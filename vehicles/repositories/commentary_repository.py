from typing import List, Optional
from django.utils import timezone
from vehicles.models import Commentary, Vehicle
from django.contrib.auth.models import User

class CommentaryRepository:
    def get_all(self) -> List[Commentary]:
        return Commentary.objects.all()
    
    def create(self, commentary: str, user: User, vehicle: Vehicle) -> Commentary:
        return Commentary.objects.create(
            commentary=commentary,
            datetime=timezone.now(),
            user=user,
            vehicle=vehicle
        )
    
    def get_by_id(self, id: int) -> Optional[Commentary]:
        try:
            commentary = Commentary.objects.get(id=id)
        except Commentary.DoesNotExist:
            commentary = None
        return commentary
    
    def update(self, commentary: Commentary, new_commentary: str) -> Commentary:
        commentary = self.get_by_id(commentary.id)
        if commentary:
            commentary.commentary = new_commentary
            commentary.save()
        return commentary

    def delete(self, commentary: Commentary):
        return commentary.delete()
