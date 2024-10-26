from rest_framework import generics
from vehicles.models import Vehicle
from vehicles.serializers import VehicleSerializer

class VehicleListCreateView(generics.ListCreateAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
