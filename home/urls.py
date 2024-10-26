from django.urls import path

from home.views import (
    LoginView,
    LogoutView,
    register,
    AdminPanelView,load_provinces,
    load_cities
)
from vehicles_dealership_system.decorators import staff_member_required

urlpatterns = [
    path(route='login/',view=LoginView.as_view(),name='login'),
    path(route='logout/', view=LogoutView.as_view(), name='logout'),
    path('register/', register, name='register'),
    path(route='admin_panel/', view=staff_member_required(AdminPanelView.as_view()), name='admin_panel'),
    path('ajax/load-provinces/', load_provinces, name='load_provinces'),
    path('ajax/load-cities/', load_cities, name='load_cities'),
]
