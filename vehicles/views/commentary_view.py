from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from vehicles.models import Commentary, Vehicle
from django.contrib.auth.models import User
from vehicles.repositories.commentary_repository import CommentaryRepository
from django.urls import reverse


@method_decorator(login_required, name='dispatch')
class CommentaryAddView(View):
    repository = CommentaryRepository()

    def post(self, request):
        commentary_text = request.POST.get('commentary')
        user_id = request.POST.get('user_id')
        vehicle_id = request.POST.get('vehicle_id') 

        user = get_object_or_404(User, id=user_id)
        vehicle = get_object_or_404(Vehicle, id=vehicle_id)

        self.repository.create(
            commentary=commentary_text,
            user=user,
            vehicle=vehicle
        )

        return redirect(reverse('vehicle_detail', args=[vehicle.id]))

@method_decorator(login_required, name='dispatch')
class CommentaryEditView(View):
    repository = CommentaryRepository()

    def get(self, request, commentary_id):
        commentary = get_object_or_404(Commentary, id=commentary_id)
        context = {
            'commentary': commentary,
            'vehicle': commentary.vehicle,
        }
        return render(request, 'commentary/edit_commentary.html', context)

    def post(self, request, commentary_id):
        commentary = get_object_or_404(Commentary, id=commentary_id)
        commentary_text = request.POST.get('commentary')
        commentary.commentary = commentary_text
        commentary.save()

        return redirect(reverse('vehicle_detail', args=[commentary.vehicle.id]))

@method_decorator(login_required, name='dispatch')
class CommentaryDeleteView(View):
    repository = CommentaryRepository()

    def get(self, request, commentary_id):
        commentary = get_object_or_404(Commentary, id=commentary_id)
        vehicle_id = commentary.vehicle.id
        commentary.delete()

        return redirect(reverse('vehicle_detail', args=[vehicle_id]))
