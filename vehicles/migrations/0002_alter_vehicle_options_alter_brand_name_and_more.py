# Generated by Django 5.0.7 on 2024-10-31 22:13

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vehicle',
            options={'verbose_name': 'Vehicle', 'verbose_name_plural': 'Vehicles'},
        ),
        migrations.AlterField(
            model_name='brand',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Brand Name'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=70, verbose_name='Category Name'),
        ),
        migrations.AlterField(
            model_name='commentary',
            name='commentary',
            field=models.CharField(max_length=50, verbose_name='Commentary'),
        ),
        migrations.AlterField(
            model_name='commentary',
            name='datetime',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Date and Time'),
        ),
        migrations.AlterField(
            model_name='commentary',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
        migrations.AlterField(
            model_name='commentary',
            name='vehicle',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vehicle', to='vehicles.vehicle', verbose_name='Vehicle'),
        ),
        migrations.AlterField(
            model_name='enginetype',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Engine Type'),
        ),
        migrations.AlterField(
            model_name='model',
            name='brand',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='brand', to='vehicles.brand', verbose_name='Brand'),
        ),
        migrations.AlterField(
            model_name='model',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category', to='vehicles.category', verbose_name='Category'),
        ),
        migrations.AlterField(
            model_name='model',
            name='engine_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='engine_type', to='vehicles.enginetype', verbose_name='Engine Type'),
        ),
        migrations.AlterField(
            model_name='model',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Model Name'),
        ),
        migrations.AlterField(
            model_name='model',
            name='steering',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='steering', to='vehicles.steering', verbose_name='Steering'),
        ),
        migrations.AlterField(
            model_name='model',
            name='traction_control',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='traction_control', to='vehicles.tractioncontrol', verbose_name='Traction Control'),
        ),
        migrations.AlterField(
            model_name='model',
            name='transmission',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transmission', to='vehicles.transmission', verbose_name='Transmission'),
        ),
        migrations.AlterField(
            model_name='model',
            name='vehicle_body_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vehicle_body_type', to='vehicles.vehiclebodytype', verbose_name='Body Type'),
        ),
        migrations.AlterField(
            model_name='steering',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Steering Type'),
        ),
        migrations.AlterField(
            model_name='tractioncontrol',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Traction Control'),
        ),
        migrations.AlterField(
            model_name='transmission',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Transmission Type'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='description',
            field=models.TextField(verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='image',
            field=models.ImageField(upload_to='vehicles/', verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='model', to='vehicles.model', verbose_name='Model'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=20, verbose_name='Price'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='vehicle_condition',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vehicle_condition', to='vehicles.vehiclecondition', verbose_name='Condition'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='year',
            field=models.IntegerField(verbose_name='Year'),
        ),
        migrations.AlterField(
            model_name='vehiclebodytype',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Body Type'),
        ),
        migrations.AlterField(
            model_name='vehiclecondition',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Condition'),
        ),
    ]
