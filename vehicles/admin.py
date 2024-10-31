from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import Vehicle

@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ('vehicle_name', 'model_name', 'brand_name', 'year', 'price')
    list_filter = ('model__brand',)

    def vehicle_name(self, obj):
        return str(obj)
    vehicle_name.short_description = _('Vehicle')

    def model_name(self, obj):
        return obj.model.name
    model_name.short_description = _('Model')

    def brand_name(self, obj):
        return obj.model.brand.name
    brand_name.short_description = _('Brand')
