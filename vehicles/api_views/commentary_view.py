from rest_framework import generics
from vehicles.models import Commentary
from vehicles.serializers import CommentarySerializer

class VehicleCommentsListView(generics.ListAPIView):
    serializer_class = CommentarySerializer

    def get_queryset(self):
        vehicle_id = self.kwargs['vehicle_id']
        return Commentary.objects.filter(vehicle_id=vehicle_id)