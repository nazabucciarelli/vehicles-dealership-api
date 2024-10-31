from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=70, verbose_name=_("Category Name"))

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=50, verbose_name=_("Brand Name"))

    def __str__(self):
        return self.name


class Transmission(models.Model):
    name = models.CharField(max_length=50, verbose_name=_("Transmission Type"))

    def __str__(self):
        return self.name


class Steering(models.Model):
    name = models.CharField(max_length=50, verbose_name=_("Steering Type"))

    def __str__(self):
        return self.name


class TractionControl(models.Model):
    name = models.CharField(max_length=50, verbose_name=_("Traction Control"))

    def __str__(self):
        return self.name


class VehicleBodyType(models.Model):
    name = models.CharField(max_length=50, verbose_name=_("Body Type"))

    def __str__(self):
        return self.name


class VehicleCondition(models.Model):
    name = models.CharField(max_length=50, verbose_name=_("Condition"))

    def __str__(self):
        return self.name


class EngineType(models.Model):
    name = models.CharField(max_length=50, verbose_name=_("Engine Type"))

    def __str__(self):
        return self.name


class Model(models.Model):
    name = models.CharField(max_length=50, verbose_name=_("Model Name"))
    brand = models.ForeignKey(
        Brand,
        on_delete=models.CASCADE,
        related_name='brand',
        verbose_name=_("Brand")
    )
    transmission = models.ForeignKey(
        Transmission,
        on_delete=models.CASCADE,
        related_name='transmission',
        verbose_name=_("Transmission")
    )
    traction_control = models.ForeignKey(
        TractionControl,
        on_delete=models.CASCADE,
        related_name='traction_control',
        verbose_name=_("Traction Control")
    )
    vehicle_body_type = models.ForeignKey(
        VehicleBodyType,
        on_delete=models.CASCADE,
        related_name='vehicle_body_type',
        verbose_name=_("Body Type")
    )
    steering = models.ForeignKey(
        Steering,
        on_delete=models.CASCADE,
        related_name='steering',
        verbose_name=_("Steering")
    )
    engine_type = models.ForeignKey(
        EngineType,
        on_delete=models.CASCADE,
        related_name='engine_type',
        verbose_name=_("Engine Type")
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='category',
        verbose_name=_("Category")
    )

    def __str__(self):
        return self.name

from django.utils.translation import gettext_lazy as _

class Vehicle(models.Model):
    description = models.TextField(
        null=False,
        blank=False,
        verbose_name=_("Description")
    )
    year = models.IntegerField(
        null=False,
        blank=False,
        verbose_name=_("Year")
    )
    price = models.DecimalField(
        max_digits=20,
        decimal_places=2,
        verbose_name=_("Price")
    )
    model = models.ForeignKey(
        Model,
        on_delete=models.CASCADE,
        related_name="model",
        verbose_name=_("Model")
    )
    vehicle_condition = models.ForeignKey(
        VehicleCondition,
        on_delete=models.CASCADE,
        related_name='vehicle_condition',
        verbose_name=_("Condition")
    )
    image = models.ImageField(upload_to='vehicles/', null=False, verbose_name=_("Image"))

    class Meta:
        verbose_name = _("Vehicle")
        verbose_name_plural = _("Vehicles")

    def __str__(self):
        return f"{self.model.name} ({self.year})"



class Commentary(models.Model):
    commentary = models.CharField(max_length=50, verbose_name=_("Commentary"))
    datetime = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("Date and Time")
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='user',
        verbose_name=_("User")
    )
    vehicle = models.ForeignKey(
        Vehicle,
        on_delete=models.CASCADE,
        related_name='vehicle',
        verbose_name=_("Vehicle")
    )

    def __str__(self):
        return self.commentary
