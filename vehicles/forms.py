# vehicles/forms.py
from django import forms
from vehicles.models import Brand, Model, VehicleCondition, EngineType, Transmission, TractionControl, VehicleBodyType, Steering, Category, Vehicle


class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }


class ModelForm(forms.ModelForm):
    class Meta:
        model = Model
        fields = ['name', 'brand', 'transmission', 'traction_control',
                  'vehicle_body_type', 'steering', 'engine_type', 'category']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'brand': forms.Select(attrs={'class': 'form-control'}),
            'transmission': forms.Select(attrs={'class': 'form-control'}),
            'traction_control': forms.Select(attrs={'class': 'form-control'}),
            'vehicle_body_type': forms.Select(attrs={'class': 'form-control'}),
            'steering': forms.Select(attrs={'class': 'form-control'}),
            'engine_type': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }


class VehicleConditionForm(forms.ModelForm):
    class Meta:
        model = VehicleCondition
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }


class EngineTypeForm(forms.ModelForm):
    class Meta:
        model = EngineType
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }


class TransmissionForm(forms.ModelForm):
    class Meta:
        model = Transmission
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }


class TractionControlForm(forms.ModelForm):
    class Meta:
        model = TractionControl
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }


class VehicleBodyTypeForm(forms.ModelForm):
    class Meta:
        model = VehicleBodyType
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }


class SteeringForm(forms.ModelForm):
    class Meta:
        model = Steering
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }


class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = ['description', 'year', 'price',
                  'image', 'model', 'vehicle_condition']
        widgets = {
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'year': forms.NumberInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control-file'}),
            'model': forms.Select(attrs={'class': 'form-control'}),
            'vehicle_condition': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(VehicleForm, self).__init__(*args, **kwargs)
        self.fields['model'].queryset = Model.objects.all()
        self.fields['model'].label_from_instance = lambda obj: f"{obj.brand.name} {obj.name}"
