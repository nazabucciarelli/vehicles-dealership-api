from django.urls import path
from vehicles.views.category_view import CategoryVehiclesListView
from vehicles.views.brand_view import BrandAddView, BrandListView, BrandEditView, BrandDeleteView
from vehicles.views.engine_type_view import EngineTypeAddView, EngineTypeDeleteView, EngineTypeListView, EngineTypeEditView
from vehicles.views.model_view import ModelAddView, ModelListView, ModelDeleteView, ModelEditView
from vehicles.views.steering_view import SteeringAddView, SteeringDeleteView, SteeringEditView, SteeringListView
from vehicles.views.traction_control_view import TractionControlAddView, TractionControlDeleteView, TractionControlEditView, TractionControlListView
from vehicles.views.transmission_view import TransmissionAddView, TransmissionDeleteView, TransmissionEditView, TransmissionListView
from vehicles.views.vehicle_body_view import VehicleBodyTypeAddView, VehicleBodyTypeDeleteView, VehicleBodyTypeEditView, VehicleBodyTypeListView
from vehicles.views.vehicle_condition_view import VehicleConditionAddView, VehicleConditionDeleteView, VehicleConditionEditView, VehicleConditionListView
from vehicles.views.vehicle_view import VehicleAddView, VehicleDeleteView, VehicleEditView, VehicleListView, VehicleListPaginatedView, VehicleDetailView
from vehicles.views.category_view import CategoryAddView, CategoryEditView, CategoryDeleteView, CategoryListView
from vehicles.views.commentary_view import CommentaryAddView, CommentaryEditView, CommentaryDeleteView
from vehicles_dealership_system.decorators import staff_member_required, user_is_comment_owner_or_staff, user_is_comment_owner

urlpatterns = [
    path('', VehicleListPaginatedView.as_view(), name='vehicle_list'),

    path('brands/', staff_member_required(BrandListView.as_view()), name='list_brand'),
    path('brands/add/', staff_member_required(BrandAddView.as_view()), name='add_brand'),
    path('brands/edit/<int:brand_id>/',
         staff_member_required(BrandEditView.as_view()), name='edit_brand'),
    path('brands/delete/<int:brand_id>/',
         staff_member_required(BrandDeleteView.as_view()), name='delete_brand'),

    path('models/', staff_member_required(ModelListView.as_view()), name='list_model'),
    path('models/add/', staff_member_required(ModelAddView.as_view()), name='add_model'),
    path('models/edit/<int:model_id>/',
         staff_member_required(ModelEditView.as_view()), name='edit_model'),
    path('models/delete/<int:model_id>/',
         staff_member_required(ModelDeleteView.as_view()), name='delete_model'),

    path('vehicle_conditions/', staff_member_required(VehicleConditionListView.as_view()),
         name='list_vehicle_condition'),
    path('vehicle_conditions/add/', staff_member_required(VehicleConditionAddView.as_view()),
         name='add_vehicle_condition'),
    path('vehicle_conditions/edit/<int:vehicle_condition_id>/',
         staff_member_required(VehicleConditionEditView.as_view()), name='edit_vehicle_condition'),
    path('vehicle_conditions/delete/<int:vehicle_condition_id>/',
         staff_member_required(VehicleConditionDeleteView.as_view()), name='delete_vehicle_condition'),

    path('engine_types/', staff_member_required(EngineTypeListView.as_view()),
         name='list_engine_type'),
    path('engine_types/add/', staff_member_required(EngineTypeAddView.as_view()),
         name='add_engine_type'),
    path('engine_types/edit/<int:engine_type_id>/',
         staff_member_required(EngineTypeEditView.as_view()), name='edit_engine_type'),
    path('engine_types/delete/<int:engine_type_id>/',
         staff_member_required(EngineTypeDeleteView.as_view()), name='delete_engine_type'),

    path('transmissions/', staff_member_required(TransmissionListView.as_view()),
         name='list_transmission'),
    path('transmissions/add/', staff_member_required(TransmissionAddView.as_view()),
         name='add_transmission'),
    path('transmissions/edit/<int:transmission_id>/',
         staff_member_required(TransmissionEditView.as_view()), name='edit_transmission'),
    path('transmissions/delete/<int:transmission_id>/',
         staff_member_required(TransmissionDeleteView.as_view()), name='delete_transmission'),

    path('traction_controls/', staff_member_required(TractionControlListView.as_view()),
         name='list_traction_control'),
    path('traction_controls/add/', staff_member_required(TractionControlAddView.as_view()),
         name='add_traction_control'),
    path('traction_controls/edit/<int:traction_control_id>/',
         staff_member_required(TractionControlEditView.as_view()), name='edit_traction_control'),
    path('traction_controls/delete/<int:traction_control_id>/',
         staff_member_required(TractionControlDeleteView.as_view()), name='delete_traction_control'),

    path('vehicle_body_types/', staff_member_required(VehicleBodyTypeListView.as_view()),
         name='list_vehicle_body_type'),
    path('vehicle_body_types/add/', staff_member_required(VehicleBodyTypeAddView.as_view()),
         name='add_vehicle_body_type'),
    path('vehicle_body_types/edit/<int:vehicle_body_type_id>/',
         staff_member_required(VehicleBodyTypeEditView.as_view()), name='edit_vehicle_body_type'),
    path('vehicle_body_types/delete/<int:vehicle_body_type_id>/',
         staff_member_required(VehicleBodyTypeDeleteView.as_view()), name='delete_vehicle_body_type'),

    path('steerings/', staff_member_required(SteeringListView.as_view()),
         name='list_steering'),
    path('steerings/add/', staff_member_required(SteeringAddView.as_view()),
         name='add_steering'),
    path('steerings/edit/<int:steering_id>/',
         staff_member_required(SteeringEditView.as_view()), name='edit_steering'),
    path('steerings/delete/<int:steering_id>/',
         staff_member_required(SteeringDeleteView.as_view()), name='delete_steering'),

    path('vehicles/', staff_member_required(VehicleListView.as_view()),
         name='list_vehicle'),
    path('vehicle/<int:id>/', VehicleDetailView.as_view(),
         name='vehicle_detail'),
    path('vehicles/add/', staff_member_required(VehicleAddView.as_view()),
         name='add_vehicle'),
    path('vehicles/edit/<int:vehicle_id>/',
         staff_member_required(VehicleEditView.as_view()), name='edit_vehicle'),
    path('vehicles/delete/<int:vehicle_id>/',
         staff_member_required(VehicleDeleteView.as_view()), name='delete_vehicle'),

    path('categories/<int:category_id>/',
         CategoryVehiclesListView.as_view(), name='category_vehicle_list'),
    path('categories/', staff_member_required(CategoryListView.as_view()),
         name='list_category'),
    path('categories/add/', staff_member_required(CategoryAddView.as_view()),
         name='add_category'),
    path('categories/edit/<int:category_id>/',
         staff_member_required(CategoryEditView.as_view()), name='edit_category'),
    path('categories/delete/<int:category_id>/',
         staff_member_required(CategoryDeleteView.as_view()), name='delete_category'),

    path('add_commentary/', CommentaryAddView.as_view(), name='add_commentary'),
    path('edit_commentary/<int:commentary_id>/',
         user_is_comment_owner(CommentaryEditView.as_view()), name='edit_commentary'),
    path('delete_commentary/<int:commentary_id>/',
         user_is_comment_owner_or_staff(CommentaryDeleteView.as_view()), name='delete_commentary'),
]
