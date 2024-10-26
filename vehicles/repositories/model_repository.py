from vehicles.models import Model, Brand, Transmission, TractionControl, EngineType, VehicleBodyType, Steering, Category
from typing import List, Optional


class ModelRepository:
    def get_all(self) -> List[Model]:
        return Model.objects.all()

    def create(self, name: str,
               brand: Brand,
               transmission: Transmission,
               traction_control: TractionControl,
               vehicle_body_type: VehicleBodyType,
               steering: Steering,
               engine_type: EngineType,
               category: Category) -> Model:
        model = Model(name=name,
                       brand=brand,
                       transmission=transmission,
                       traction_control=traction_control,
                       vehicle_body_type=vehicle_body_type,
                       steering=steering,
                       engine_type=engine_type,
                       category=category)
        model.save()
        return model

    def get_by_id(self, id: int) -> Optional[Model]:
        try:
            model = Model.objects.get(id=id)
        except:
            model = None
        return model

    def update(self, model: Model, name: str) -> Model: # TO-DO
        model = self.get_by_id(model.id)
        model.name = name
        model.save()
        return model

    def delete(self, model: Model):
        return model.delete()
