# Generated by Django 3.2.18 on 2023-05-08 12:31

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0018_alter_sessionbook_booked_slot'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sessionbook',
            name='age',
            field=models.IntegerField(default=18, validators=[django.core.validators.MinValueValidator(18), django.core.validators.MaxValueValidator(80)], verbose_name='Age'),
        ),
        migrations.AlterField(
            model_name='sessionbook',
            name='booked_slot',
            field=models.CharField(choices=[('10 AM', '10 AM'), ('2 PM', '2 PM'), ('8 PM', '8 PM'), ('8 AM', '8 AM'), ('4 PM', '4 PM'), ('12 PM', '12 PM'), ('6 PM', '6 PM')], default='8 AM', max_length=10, verbose_name='Pick a Slot'),
        ),
        migrations.AlterField(
            model_name='sessionbook',
            name='client_notes',
            field=models.TextField(blank=True, verbose_name='Leave Your Request Here'),
        ),
        migrations.AlterField(
            model_name='sessionbook',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='E-Mail'),
        ),
        migrations.AlterField(
            model_name='sessionbook',
            name='fname',
            field=models.CharField(blank=True, max_length=15, verbose_name='First Name'),
        ),
        migrations.AlterField(
            model_name='sessionbook',
            name='lname',
            field=models.CharField(blank=True, max_length=15, verbose_name='Last Name'),
        ),
        migrations.AlterField(
            model_name='sessionbook',
            name='phone',
            field=models.CharField(max_length=15, verbose_name='Phone No.'),
        ),
    ]
