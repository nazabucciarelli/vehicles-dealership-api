from django.shortcuts import render, redirect
from django.views import View
from vehicles.forms import TransmissionForm
from vehicles.repositories.transmission_repository import TransmissionRepository

class TransmissionAddView(View):
    def get(self, request):
        form = TransmissionForm()
        return render(request, 'transmission/add_transmission.html', {'form': form})

    def post(self, request):
        form = TransmissionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_panel')
        return render(request, 'transmission/add_transmission.html', {'form': form})
    
class TransmissionListView(View):
    transmission_repository = TransmissionRepository()

    def get(self, request):
        transmissions = self.transmission_repository.get_all()
        return render(request, 'transmission/list_transmission.html', {'transmissions': transmissions})

class TransmissionEditView(View):
    transmission_repository = TransmissionRepository()

    def get(self, request, transmission_id):
        transmission = self.transmission_repository.get_by_id(id=transmission_id)
        form = TransmissionForm(instance=transmission)
        return render(request, 'transmission/edit_transmission.html', {'form': form})

    def post(self, request, transmission_id):
        transmission = self.transmission_repository.get_by_id(id=transmission_id)
        form = TransmissionForm(request.POST, instance=transmission)
        if form.is_valid():
            form.save()
            return redirect('list_transmission')
        return render(request, 'transmission/edit_transmission.html', {'form': form})

class TransmissionDeleteView(View):
    transmission_repository = TransmissionRepository()

    def post(self, request, transmission_id):
        transmission = self.transmission_repository.get_by_id(id=transmission_id)
        transmission.delete()
        return redirect('list_transmission')