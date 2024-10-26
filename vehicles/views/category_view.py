from django.shortcuts import render, redirect

from vehicles.repositories.category_repository import CategoryRepository
from vehicles.repositories.vehicle_repository import VehicleRepository
from django.views import View
from vehicles.forms import CategoryForm

class CategoryAddView(View):
    def get(self, request):
        form = CategoryForm()
        return render(request, 'category/add_category.html', {'form': form})

    def post(self, request):
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_panel')
        return render(request, 'category/add_category.html', {'form': form})

class CategoryVehiclesListView(View):
    category_repository = CategoryRepository()
    vehicle_repository = VehicleRepository()

    def get(self, request, category_id):
        category = self.category_repository.get_by_id(id=category_id)
        vehicles = self.vehicle_repository.get_by_category(category=category)
        return render(request,
                      'category/category_vehicles_list.html',
                      {'category': category, 'vehicles': vehicles})

class CategoryListView(View):
    category_repository = CategoryRepository()

    def get(self, request):
        categories = self.category_repository.get_all()
        return render(request, 'category/list_category.html', {'categories': categories})

class CategoryEditView(View):
    category_repository = CategoryRepository()

    def get(self, request, category_id):
        category = self.category_repository.get_by_id(id=category_id)
        form = CategoryForm(instance=category)
        return render(request, 'category/edit_category.html', {'form': form})

    def post(self, request, category_id):
        category = self.category_repository.get_by_id(id=category_id)
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('list_category')
        return render(request, 'category/edit_category.html', {'form': form})

class CategoryDeleteView(View):
    category_repository = CategoryRepository()

    def post(self, request, category_id):
        brand = self.category_repository.get_by_id(id=category_id)
        brand.delete()
        return redirect('list_category')