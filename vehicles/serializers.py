from rest_framework import serializers
from vehicles.models import Brand
from vehicles.models import Vehicle
from vehicles.models import Commentary
from vehicles.models import Model
from vehicles.models import Category
from vehicles.models import Steering
from vehicles.models import TractionControl
from vehicles.models import Steering
from vehicles.models import Transmission
from vehicles.models import EngineType
from vehicles.models import VehicleBodyType
from vehicles.models import VehicleCondition

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class SteeringSerializer(serializers.ModelSerializer):
    class Meta:
        model = Steering
        fields = '__all__'

class TractionControlSerializer(serializers.ModelSerializer):
    class Meta:
        model = TractionControl
        fields = '__all__'

class TransmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transmission
        fields = '__all__'

class EngineTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EngineType
        fields = '__all__'

class VehicleBodyTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleBodyType
        fields = '__all__'

class ModelSerializer(serializers.ModelSerializer):
    brand = BrandSerializer()
    category = CategorySerializer()
    steering = SteeringSerializer()
    traction_control = TractionControlSerializer()
    transmission = TransmissionSerializer()
    engine_type = EngineTypeSerializer()
    vehicle_body_type = VehicleBodyTypeSerializer()

    class Meta:
        model = Model
        fields = '__all__'


class VehicleConditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleCondition
        fields = '__all__'

class VehicleSerializer(serializers.ModelSerializer):
    model = ModelSerializer()
    vehicle_condition = VehicleConditionSerializer()

    class Meta:
        model = Vehicle
        fields = '__all__'


class CommentarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Commentary
        fields = '__all__'