from typing import List, Optional
from vehicles.models import Transmission

class TransmissionRepository:
    def get_all(self) -> List[Transmission]:
        return Transmission.objects.all()
    
    def create(self, name: str) -> Transmission:
        return Transmission.objects.create(name=name)
    
    def get_by_id(self, id: int) -> Optional[Transmission]:
        try:
            transmission = Transmission.objects.get(id=id)
        except Transmission.DoesNotExist:
            transmission = None
        return transmission
    
    def update(self, transmission: Transmission, name: str) -> Transmission:
        transmission.name = name
        transmission.save()
        return transmission

    def delete(self, transmission: Transmission):
        return transmission.delete()
