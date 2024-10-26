from django.urls import path
from users.api_views.user_view import UserListCreateView
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('api/users/',
         UserListCreateView.as_view(), name='users_list_create'),
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
]
