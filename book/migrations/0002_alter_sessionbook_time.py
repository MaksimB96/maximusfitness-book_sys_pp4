# Generated by Django 3.2.18 on 2023-05-16 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sessionbook',
            name='time',
            field=models.TimeField(choices=[('10:00', '10:00 AM'), ('19:00', '19:00 AM'), ('13:00', '13:00 PM'), ('15:00', '15:00 AM'), ('08:00', '8:00 AM'), ('17:00', '17:00 AM')], verbose_name='Pick a Time'),
        ),
    ]