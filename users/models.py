from django.contrib.auth.models import User
from django.db import models


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
        related_name='country',
        null=False
    )

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=255)
    province = models.ForeignKey(
        Province,
        on_delete=models.CASCADE,
        related_name='province',
        null=False
    )

    def __str__(self):
        return self.name


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    id_number = models.CharField(max_length=15)
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE, related_name='gender')
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='city')

    def __str__(self):
        return self.user.username