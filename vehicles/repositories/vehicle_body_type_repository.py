from typing import List, Optional
from vehicles.models import VehicleBodyType

class VehicleBodyTypeRepository:
    def get_all(self) -> List[VehicleBodyType]:
        return VehicleBodyType.objects.all()
    
    def create(self, name: str) -> VehicleBodyType:
        return VehicleBodyType.objects.create(name=name)
    
    def get_by_id(self, id: int) -> Optional[VehicleBodyType]:
        try:
            vehicle_body_type = VehicleBodyType.objects.get(id=id)
        except VehicleBodyType.DoesNotExist:
            vehicle_body_type = None
        return vehicle_body_type
    
    def update(self, vehicle_body_type: VehicleBodyType, name: str) -> VehicleBodyType:
        vehicle_body_type.name = name
        vehicle_body_type.save()
        return vehicle_body_type

    def delete(self, vehicle_body_type: VehicleBodyType):
        return vehicle_body_type.delete()
