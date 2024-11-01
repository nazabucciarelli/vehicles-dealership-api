from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _

class Gender(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Country(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Province(models.Model):
    name = models.CharField(max_length=255)
    country = models.ForeignKey(
        Country,
        on_delete=models.CASCADE,
        related_name='province',
        null=False
    )

    def __str__(self):
        return self.name

class City(models.Model):
    name = models.CharField(max_length=255)
    province = models.ForeignKey(
        Province,
        on_delete=models.CASCADE,
        related_name='city',
        null=False
    )

    def __str__(self):
        return self.name

class Customer(models.Model):
    LANGUAGES = [
        ('en', _('English')),
        ('es', _('Spanish')),
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name=_("name"))
    address = models.CharField(max_length=255, verbose_name=_("address"))
    phone_number = models.CharField(max_length=15, verbose_name=_("phone_number"))
    id_number = models.CharField(max_length=15)
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE, related_name='gender', verbose_name=_("gender"))
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='city', verbose_name=_("city"))
    language = models.CharField(max_length=2, choices=LANGUAGES, default='es', verbose_name=_("Language"))

    def __str__(self):
        return self.user.username
