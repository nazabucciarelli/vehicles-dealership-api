from typing import List, Optional

from vehicles.models import Category

class CategoryRepository:
    def get_all(self) -> List[Category]:
        return Category.objects.all()
    
    def create(self,name:str) -> Category:
        return Category.objects.create(name=name)
    
    def get_by_id(self,id:int) -> Optional[Category]:
        try:
            category = Category.objects.get(id=id)
        except:
            category = None
        return category
    
    def update(self,category:Category,name:str) -> Category:
        category = self.get_by_id(category.id)
        category.name = name
        category.save() 
        return category

    def delete(self,category: Category):
        return category.delete()