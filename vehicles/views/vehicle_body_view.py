from django.shortcuts import render, redirect
from django.views import View
from vehicles.forms import VehicleBodyTypeForm
from vehicles.repositories.vehicle_body_type_repository import VehicleBodyTypeRepository

class VehicleBodyTypeAddView(View):
    def get(self, request):
        form = VehicleBodyTypeForm()
        return render(request, 'vehicle_body_type/add_vehicle_body_type.html', {'form': form})

    def post(self, request):
        form = VehicleBodyTypeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_panel')
        return render(request, 'vehicle_body_type/add_vehicle_body_type.html', {'form': form})

class VehicleBodyTypeListView(View):
    vehicle_body_type_repository = VehicleBodyTypeRepository()

    def get(self, request):
        vehicle_body_types = self.vehicle_body_type_repository.get_all()
        return render(request, 'vehicle_body_type/list_vehicle_body_type.html', {'vehicle_body_types': vehicle_body_types})

class VehicleBodyTypeEditView(View):
    vehicle_body_type_repository = VehicleBodyTypeRepository()

    def get(self, request, vehicle_body_type_id):
        vehicle_body_type = self.vehicle_body_type_repository.get_by_id(id=vehicle_body_type_id)
        form = VehicleBodyTypeForm(instance=vehicle_body_type)
        return render(request, 'vehicle_body_type/edit_vehicle_body_type.html', {'form': form})

    def post(self, request, vehicle_body_type_id):
        vehicle_body_type = self.vehicle_body_type_repository.get_by_id(id=vehicle_body_type_id)
        form = VehicleBodyTypeForm(request.POST, instance=vehicle_body_type)
        if form.is_valid():
            form.save()
            return redirect('list_vehicle_body_type')
        return render(request, 'vehicle_body_type/edit_vehicle_body_type.html', {'form': form})

class VehicleBodyTypeDeleteView(View):
    vehicle_body_type_repository = VehicleBodyTypeRepository()

    def post(self, request, vehicle_body_type_id):
        vehicle_body_type = self.vehicle_body_type_repository.get_by_id(id=vehicle_body_type_id)
        vehicle_body_type.delete()
        return redirect('list_vehicle_body_type')