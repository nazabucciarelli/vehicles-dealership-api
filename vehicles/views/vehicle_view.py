from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required

from django.views import View
from django.views.generic.detail import DetailView
from django.shortcuts import get_object_or_404
from django.views.generic import ListView
from vehicles.models import Vehicle, Commentary
from vehicles.forms import VehicleForm
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


class VehicleDetailView(DetailView):
    model = Vehicle
    template_name = 'vehicle/vehicle_detail.html'
    context_object_name = 'vehicle'

    def get_object(self):
        vehicle_id = self.kwargs.get('id')
        return get_object_or_404(Vehicle, id=vehicle_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
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
