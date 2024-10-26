from typing import List, Optional
from vehicles.models import EngineType

class EngineTypeRepository:
    def get_all(self) -> List[EngineType]:
        return EngineType.objects.all()
    
    def create(self, name: str) -> EngineType:
        return EngineType.objects.create(name=name)
    
    def get_by_id(self, id: int) -> Optional[EngineType]:
        try:
            engine_type = EngineType.objects.get(id=id)
        except EngineType.DoesNotExist:
            engine_type = None
        return engine_type
    
    def update(self, engine_type: EngineType, name: str) -> EngineType:
        engine_type.name = name
        engine_type.save()
        return engine_type

    def delete(self, engine_type: EngineType):
        return engine_type.delete()
