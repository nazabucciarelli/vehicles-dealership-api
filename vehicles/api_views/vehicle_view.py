from rest_framework import generics
from vehicles.models import Vehicle
from vehicles.serializers import VehicleSerializer
from vehicles_dealership_system.permissions import IsStaffForCreate

class VehicleListCreateView(generics.ListCreateAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

    permission_classes = [IsStaffForCreate]
