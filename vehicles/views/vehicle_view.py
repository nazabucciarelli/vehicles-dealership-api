from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.translation import (
    activate,
    deactivate,
    get_language,
    gettext_lazy as _,
)
from django.views import View
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from vehicles.forms import VehicleForm
from vehicles.models import Vehicle, Commentary
from users.models import Customer
from vehicles.repositories.vehicle_repository import VehicleRepository


class VehicleAddView(View):
    def get(self, request):
        form = VehicleForm()
        return render(request, 'vehicle/add_vehicle.html', {'form': form})

    def post(self, request):
        form = VehicleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admin_panel')
        return render(request, 'vehicle/add_vehicle.html', {'form': form})

class UpdateLang(View):
    def get(self, request):
        if request.user.is_authenticated:
            customer = get_object_or_404(Customer, user=request.user)
            if customer.language == 'es':
                customer.language = 'en'
            else:
                customer.language = 'es'
            customer.save()
            activate(customer.language)
        
        else:
            current_language = get_language()
            new_language = 'en' if current_language == 'es' else 'es'
            activate(new_language)

        return redirect(request.META.get('HTTP_REFERER', 'index'))


class VehicleDetailView(DetailView):
    model = Vehicle
    template_name = 'vehicle/vehicle_detail.html'
    context_object_name = 'vehicle'

    def get_object(self):
        vehicle_id = self.kwargs.get('id')
        return get_object_or_404(Vehicle, id=vehicle_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        user_language = 'es'
        if self.request.user.is_authenticated:
            try:
                customer = Customer.objects.get(user=self.request.user.id)
                user_language = customer.language
                activate(customer.language)
            except Customer.DoesNotExist:
                activate('es')
        else:
            current_language = get_language()
            if current_language == 'en':
                user_language = 'en'
            else:
                user_language = 'es'
        
        context['user_language'] = user_language
        
        vehicle = self.get_object()
        comments = Commentary.objects.filter(vehicle=vehicle)
        context['comments'] = comments
        
        return context



class VehicleListPaginatedView(ListView):
    model = Vehicle
    template_name = 'index.html'
    context_object_name = 'vehicles'
    paginate_by = 9


class VehicleListView(View):
    vehicle_repository = VehicleRepository()

    def get(self, request):
        vehicles = self.vehicle_repository.get_all()
        return render(request, 'vehicle/list_vehicle.html', {'vehicles': vehicles})


class VehicleEditView(View):
    vehicle_repository = VehicleRepository()

    def get(self, request, vehicle_id):
        vehicle = self.vehicle_repository.get_by_id(id=vehicle_id)
        form = VehicleForm(instance=vehicle)
        return render(request, 'vehicle/edit_vehicle.html', {'form': form})

    def post(self, request, vehicle_id):
        vehicle = self.vehicle_repository.get_by_id(id=vehicle_id)
        form = VehicleForm(request.POST, instance=vehicle)
        if form.is_valid():
            form.save()
            return redirect('list_vehicle')
        return render(request, 'vehicle/edit_vehicle.html', {'form': form})


class VehicleDeleteView(View):
    vehicle_repository = VehicleRepository()

    def post(self, request, vehicle_id):
        vehicle = self.vehicle_repository.get_by_id(id=vehicle_id)
        vehicle.delete()
        return redirect('list_vehicle')
