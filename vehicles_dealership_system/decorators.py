
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import get_object_or_404, redirect
from functools import wraps
from vehicles.models import Commentary
from django.urls import reverse

def staff_member_required(view_func):
    """
    Decorador que verifica si el usuario está autenticado y es miembro del personal.
    """
    actual_decorator = user_passes_test(
        lambda u: u.is_authenticated and u.is_staff,
        login_url='vehicle_list'
    )
    return actual_decorator(view_func)


def user_is_comment_owner_or_staff(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        commentary_id = kwargs.get('commentary_id')
        commentary = get_object_or_404(Commentary, id=commentary_id)
        if commentary.user == request.user or request.user.is_staff:
            return view_func(request, *args, **kwargs)
        return redirect('vehicle_detail', vehicle_id=commentary.vehicle.id)
    return _wrapped_view


def user_is_comment_owner(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        commentary_id = kwargs.get('commentary_id')
        commentary = get_object_or_404(Commentary, id=commentary_id)
        if commentary.user == request.user:
            return view_func(request, *args, **kwargs)
        return redirect(reverse('vehicle_detail', args=[commentary.vehicle.id]))
    return _wrapped_view
