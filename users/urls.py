from django.urls import path
from users.api_views.user_view import UserListCreateView

urlpatterns = [
    path('api/users/',
         UserListCreateView.as_view(), name='users_list_create'),
]
