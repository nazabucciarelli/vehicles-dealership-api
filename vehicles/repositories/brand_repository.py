from typing import List, Optional

from vehicles.models import Brand

class BrandRepository:
    def get_all(self) -> List[Brand]:
        return Brand.objects.all()
    
    def create(self,name:str) -> Brand:
        return Brand.objects.create(name=name)
    
    def get_by_id(self,id:int) -> Optional[Brand]:
        try:
            brand = Brand.objects.get(id=id)
        except:
            brand = None
        return brand
    
    def update(self,brand:Brand,name:str) -> Brand:
        brand = self.get_by_id(brand.id)
        brand.name = name
        brand.save() 
        return brand

    def delete(self,brand: Brand):
        return brand.delete()