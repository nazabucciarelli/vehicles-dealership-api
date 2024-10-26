from rest_framework import generics
from vehicles.models import Brand
from vehicles.serializers import BrandSerializer

class BrandListCreateView(generics.ListCreateAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
