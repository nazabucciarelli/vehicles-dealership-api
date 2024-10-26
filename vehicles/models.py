from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=70)

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Transmission(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Steering(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class TractionControl(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class VehicleBodyType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class VehicleCondition(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class EngineType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Model(models.Model):
    name = models.CharField(max_length=50)
    brand = models.ForeignKey(
        Brand,
        on_delete=models.CASCADE,
        related_name='brand',
        null=False
    )
    transmission = models.ForeignKey(
        Transmission,
        on_delete=models.CASCADE,
        related_name='transmission',
        null=False
    )
    traction_control = models.ForeignKey(
        TractionControl,
        on_delete=models.CASCADE,
        related_name='traction_control',
        null=False
    )
    vehicle_body_type = models.ForeignKey(
        VehicleBodyType,
        on_delete=models.CASCADE,
        related_name='vehicle_body_type',
        null=False
    )
    steering = models.ForeignKey(
        Steering,
        on_delete=models.CASCADE,
        related_name='steering',
        null=False
    )
    engine_type = models.ForeignKey(
        EngineType,
        on_delete=models.CASCADE,
        related_name='engine_type',
        null=False
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='category',
        null=False
    )

    def __str__(self):
        return self.name


class Vehicle(models.Model):
    description = models.TextField(
        null=False,
        blank=False,
    )
    year = models.IntegerField(
        null=False,
        blank=False,
    )
    price = models.DecimalField(
        max_digits=20,
        decimal_places=2,
    )
    model = models.ForeignKey(
        Model,
        on_delete=models.CASCADE,
        related_name="model",
        null=False,
    )
    vehicle_condition = models.ForeignKey(
        VehicleCondition,
        on_delete=models.CASCADE,
        related_name='vehicle_condition',
        null=False,
    )
    image = models.ImageField(upload_to='vehicles/', null=False)

    def __str__(self):
        return self.name


class Commentary(models.Model):
    commentary = models.CharField(max_length=50)
    datetime = models.DateTimeField(
        auto_now_add=True
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='user',
        null=False
    )
    vehicle = models.ForeignKey(
        Vehicle,
        on_delete=models.CASCADE,
        related_name='vehicle',
        null=False
    )

    def __str__(self):
        return self.commentary
