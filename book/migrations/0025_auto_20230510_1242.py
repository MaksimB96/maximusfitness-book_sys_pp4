# Generated by Django 3.2.18 on 2023-05-10 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0024_auto_20230510_1054'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sessionbook',
            name='booked_slot',
        ),
        migrations.AddField(
            model_name='sessionbook',
            name='time',
            field=models.CharField(choices=[('12 PM', '12 PM'), ('2 PM', '2 PM'), ('6 PM', '6 PM'), ('10 AM', '10 AM'), ('4 PM', '4 PM'), ('8 PM', '8 PM'), ('8 AM', '8 AM')], default='8 AM', max_length=10, verbose_name='Pick a Slot'),
        ),
    ]