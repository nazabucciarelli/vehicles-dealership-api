from vehicles.models import VehicleCondition
from typing import List, Optional


class VehicleConditionRepository:
    def get_all(self) -> List[VehicleCondition]:
        return VehicleCondition.objects.all()

    def create(self, name: str) -> VehicleCondition:
        return VehicleCondition.objects.create(name=name)

    def get_by_id(self, id: int) -> Optional[VehicleCondition]:
        try:
            vehicle_condition = VehicleCondition.objects.get(id=id)
        except:
            vehicle_condition = None
        return vehicle_condition

    def update(self, vehicle_condition: VehicleCondition, name: str) -> VehicleCondition:
        vehicle_condition = self.get_by_id(vehicle_condition.id)
        vehicle_condition.name = name
        vehicle_condition.save()
        return vehicle_condition

    def delete(self, vehicle_condition: VehicleCondition):
        return vehicle_condition.delete()
