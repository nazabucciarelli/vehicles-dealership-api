from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required
from django.views import View
from vehicles.forms import ModelForm
from vehicles.repositories.model_repository import ModelRepository

class ModelAddView(View):
    def get(self, request):
        form = ModelForm()
        return render(request, 'model/add_model.html', {'form': form})

    def post(self, request):
        form = ModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_panel')
        return render(request, 'model/add_model.html', {'form': form})

class ModelListView(View):
    model_repository = ModelRepository()

    def get(self, request):
        models = self.model_repository.get_all()
        return render(request, 'model/list_model.html', {'models': models})

class ModelEditView(View):
    model_repository = ModelRepository()

    def get(self, request, model_id):
        model = self.model_repository.get_by_id(id=model_id)
        form = ModelForm(instance=model)
        return render(request, 'model/edit_model.html', {'form': form})

    def post(self, request, model_id):
        model = self.model_repository.get_by_id(id=model_id)
        form = ModelForm(request.POST, instance=model)
        if form.is_valid():
            form.save()
            return redirect('list_model')
        return render(request, 'model/edit_model.html', {'form': form})

class ModelDeleteView(View):
    model_repository = ModelRepository()

    def post(self, request, model_id):
        model = self.model_repository.get_by_id(id=model_id)
        model.delete()
        return redirect('list_model')