from typing import List, Optional
from vehicles.models import Steering

class SteeringRepository:
    def get_all(self) -> List[Steering]:
        return Steering.objects.all()
    
    def create(self, name: str) -> Steering:
        return Steering.objects.create(name=name)
    
    def get_by_id(self, id: int) -> Optional[Steering]:
        try:
            steering = Steering.objects.get(id=id)
        except Steering.DoesNotExist:
            steering = None
        return steering
    
    def update(self, steering: Steering, name: str) -> Steering:
        steering.name = name
        steering.save()
        return steering

    def delete(self, steering: Steering):
        return steering.delete()
