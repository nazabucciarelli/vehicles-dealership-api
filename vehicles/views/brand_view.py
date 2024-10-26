# vehicles/views.py
from django.shortcuts import render, redirect
from django.views import View
from vehicles.forms import BrandForm
from vehicles.repositories.brand_repository import BrandRepository

class BrandAddView(View):
    def get(self, request):
        form = BrandForm()
        return render(request, 'brand/add_brand.html', {'form': form})

    def post(self, request):
        form = BrandForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_panel')
        return render(request, 'brand/add_brand.html', {'form': form})

class BrandListView(View):
    brand_repository = BrandRepository()

    def get(self, request):
        brands = self.brand_repository.get_all()
        return render(request, 'brand/list_brand.html', {'brands': brands})

class BrandEditView(View):
    brand_repository = BrandRepository()

    def get(self, request, brand_id):
        brand = self.brand_repository.get_by_id(id=brand_id)
        form = BrandForm(instance=brand)
        return render(request, 'brand/edit_brand.html', {'form': form})

    def post(self, request, brand_id):
        brand = self.brand_repository.get_by_id(id=brand_id)
        form = BrandForm(request.POST, instance=brand)
        if form.is_valid():
            form.save()
            return redirect('list_brand')
        return render(request, 'brand/edit_brand.html', {'form': form})

class BrandDeleteView(View):
    brand_repository = BrandRepository()

    def post(self, request, brand_id):
        brand = self.brand_repository.get_by_id(id=brand_id)
        brand.delete()
        return redirect('list_brand')

