from rest_framework import generics
from users.models import User
from users.serializers import UserSerializer
from vehicles_dealership_system.permissions import IsStaffForCreate

class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    permission_classes = [IsStaffForCreate]
