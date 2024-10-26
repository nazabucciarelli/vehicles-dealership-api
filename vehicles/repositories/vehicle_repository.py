from typing import List, Optional

from vehicles.models import Vehicle, VehicleCondition, Category
from django.core.files.uploadedfile import InMemoryUploadedFile


class VehicleRepository:
    def get_all(self) -> List[Vehicle]:
        return Vehicle.objects.all()

    def get_by_category(self, category: Category) -> List[Vehicle]:
        return Vehicle.objects.filter(model__category=category)

    def create(self,
               description: str,
               year: int,
               price: float,
               vehicle_condition: VehicleCondition = None,
               image: InMemoryUploadedFile = None) -> Vehicle:
        vehicle = Vehicle(description=description,
                          year=year,
                          price=price,
                          vehicle_condition=vehicle_condition)
        if image:
            vehicle.image.save(image.name, image)
        vehicle.save()
        return vehicle

    def get_by_id(self, id: int) -> Optional[Vehicle]:
        try:
            vehicle = Vehicle.objects.get(id=id)
        except:
            vehicle = None
        return vehicle

    def update(self, vehicle: Vehicle, name: str) -> Vehicle:  # To-do
        vehicle = self.get_by_id(vehicle.id)
        vehicle.save()
        return vehicle

    def delete(self, vehicle: Vehicle):
        return vehicle.delete()
