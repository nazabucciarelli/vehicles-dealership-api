from django.shortcuts import render, redirect
from django.views import View
from vehicles.forms import SteeringForm
from vehicles.repositories.steering_repository import SteeringRepository

class SteeringAddView(View):
    def get(self, request):
        form = SteeringForm()
        return render(request, 'steering/add_steering.html', {'form': form})

    def post(self, request):
        form = SteeringForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_panel')
        return render(request, 'steering/add_steering.html', {'form': form})
    
class SteeringListView(View):
    steering_repository = SteeringRepository()

    def get(self, request):
        steerings = self.steering_repository.get_all()
        return render(request, 'steering/list_steering.html', {'steerings': steerings})

class SteeringEditView(View):
    steering_repository = SteeringRepository()

    def get(self, request, steering_id):
        steering = self.steering_repository.get_by_id(id=steering_id)
        form = SteeringForm(instance=steering)
        return render(request, 'steering/edit_steering.html', {'form': form})

    def post(self, request, steering_id):
        steering = self.steering_repository.get_by_id(id=steering_id)
        form = SteeringForm(request.POST, instance=steering)
        if form.is_valid():
            form.save()
            return redirect('list_steering')
        return render(request, 'steering/edit_steering.html', {'form': form})

class SteeringDeleteView(View):
    steering_repository = SteeringRepository()

    def post(self, request, steering_id):
        steering = self.steering_repository.get_by_id(id=steering_id)
        steering.delete()
        return redirect('list_steering')