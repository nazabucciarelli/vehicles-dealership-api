from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required
from django.views import View
from vehicles.forms import VehicleConditionForm
from vehicles.repositories.vehicle_condition_repository import VehicleConditionRepository
    
class VehicleConditionAddView(View):
    def get(self, request):
        form = VehicleConditionForm()
        return render(request, 'vehicle_condition/add_vehicle_condition.html', {'form': form})

    def post(self, request):
        form = VehicleConditionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_panel')
        return render(request, 'vehicle_condition/add_vehicle_condition.html', {'form': form})

class VehicleConditionListView(View):
    vehicle_condition_repository = VehicleConditionRepository()

    def get(self, request):
        vehicle_conditions = self.vehicle_condition_repository.get_all()
        return render(request, 'vehicle_condition/list_vehicle_condition.html', {'vehicle_conditions': vehicle_conditions})

class VehicleConditionEditView(View):
    vehicle_condition_repository = VehicleConditionRepository()

    def get(self, request, vehicle_condition_id):
        vehicle_condition = self.vehicle_condition_repository.get_by_id(id=vehicle_condition_id)
        form = VehicleConditionForm(instance=vehicle_condition)
        return render(request, 'vehicle_condition/edit_vehicle_condition.html', {'form': form})

    def post(self, request, vehicle_condition_id):
        vehicle_condition = self.vehicle_condition_repository.get_by_id(id=vehicle_condition_id)
        form = VehicleConditionForm(request.POST, instance=vehicle_condition)
        if form.is_valid():
            form.save()
            return redirect('list_vehicle_condition')
        return render(request, 'vehicle_condition/edit_vehicle_condition.html', {'form': form})

class VehicleConditionDeleteView(View):
    vehicle_condition_repository = VehicleConditionRepository()

    def post(self, request, vehicle_condition_id):
        vehicle_condition = self.vehicle_condition_repository.get_by_id(id=vehicle_condition_id)
        vehicle_condition.delete()
        return redirect('list_vehicle_condition')