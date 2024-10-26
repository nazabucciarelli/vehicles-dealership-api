from django.shortcuts import render, redirect
from django.views import View
from vehicles.forms import EngineTypeForm
from vehicles.repositories.engine_type_repository import EngineTypeRepository

class EngineTypeAddView(View):
    def get(self, request):
        form = EngineTypeForm()
        return render(request, 'engine_type/add_engine_type.html', {'form': form})

    def post(self, request):
        form = EngineTypeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_panel')
        return render(request, 'engine_type/add_engine_type.html', {'form': form})

class EngineTypeListView(View):
    engine_type_repository = EngineTypeRepository()

    def get(self, request):
        engine_types = self.engine_type_repository.get_all()
        return render(request, 'engine_type/list_engine_type.html', {'engine_types': engine_types})

class EngineTypeEditView(View):
    engine_type_repository = EngineTypeRepository()

    def get(self, request, engine_type_id):
        engine_type = self.engine_type_repository.get_by_id(id=engine_type_id)
        form = EngineTypeForm(instance=engine_type)
        return render(request, 'engine_type/edit_engine_type.html', {'form': form})

    def post(self, request, engine_type_id):
        engine_type = self.engine_type_repository.get_by_id(id=engine_type_id)
        form = EngineTypeForm(request.POST, instance=engine_type)
        if form.is_valid():
            form.save()
            return redirect('list_engine_type')
        return render(request, 'engine_type/edit_engine_type.html', {'form': form})

class EngineTypeDeleteView(View):
    engine_type_repository = EngineTypeRepository()

    def post(self, request, engine_type_id):
        engine_type = self.engine_type_repository.get_by_id(id=engine_type_id)
        engine_type.delete()
        return redirect('list_engine_type')