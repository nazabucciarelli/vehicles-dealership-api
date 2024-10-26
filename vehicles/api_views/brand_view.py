from rest_framework import generics
from vehicles.models import Brand
from vehicles.serializers import BrandSerializer
from vehicles_dealership_system.permissions import IsStaffForCreate

class BrandListCreateView(generics.ListCreateAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    permission_classes = [IsStaffForCreate]
