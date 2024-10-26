from django.shortcuts import render, redirect
from django.views import View
from vehicles.forms import TractionControlForm
from vehicles.repositories.traction_control_repository import TractionControlRepository

class TractionControlAddView(View):
    def get(self, request):
        form = TractionControlForm()
        return render(request, 'traction_control/add_traction_control.html', {'form': form})

    def post(self, request):
        form = TractionControlForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_panel')
        return render(request, 'traction_control/add_traction_control.html', {'form': form})
    
class TractionControlListView(View):
    traction_control_repository = TractionControlRepository()

    def get(self, request):
        traction_controls = self.traction_control_repository.get_all()
        return render(request, 'traction_control/list_traction_control.html', {'traction_controls': traction_controls})

class TractionControlEditView(View):
    traction_control_repository = TractionControlRepository()

    def get(self, request, traction_control_id):
        traction_control = self.traction_control_repository.get_by_id(id=traction_control_id)
        form = TractionControlForm(instance=traction_control)
        return render(request, 'traction_control/edit_traction_control.html', {'form': form})

    def post(self, request, traction_control_id):
        traction_control = self.traction_control_repository.get_by_id(id=traction_control_id)
        form = TractionControlForm(request.POST, instance=traction_control)
        if form.is_valid():
            form.save()
            return redirect('list_traction_control')
        return render(request, 'traction_control/edit_traction_control.html', {'form': form})

class TractionControlDeleteView(View):
    traction_control_repository = TractionControlRepository()

    def post(self, request, traction_control_id):
        traction_control = self.traction_control_repository.get_by_id(id=traction_control_id)
        traction_control.delete()
        return redirect('list_traction_control')