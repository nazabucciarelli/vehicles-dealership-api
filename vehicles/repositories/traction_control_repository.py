from typing import List, Optional
from vehicles.models import TractionControl

class TractionControlRepository:
    def get_all(self) -> List[TractionControl]:
        return TractionControl.objects.all()
    
    def create(self, name: str) -> TractionControl:
        return TractionControl.objects.create(name=name)
    
    def get_by_id(self, id: int) -> Optional[TractionControl]:
        try:
            traction_control = TractionControl.objects.get(id=id)
        except TractionControl.DoesNotExist:
            traction_control = None
        return traction_control
    
    def update(self, traction_control: TractionControl, name: str) -> TractionControl:
        traction_control.name = name
        traction_control.save()
        return traction_control

    def delete(self, traction_control: TractionControl):
        return traction_control.delete()
