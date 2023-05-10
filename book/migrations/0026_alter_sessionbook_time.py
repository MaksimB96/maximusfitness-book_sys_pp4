# Generated by Django 3.2.18 on 2023-05-10 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0025_auto_20230510_1242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sessionbook',
            name='time',
            field=models.CharField(choices=[('6 PM', '6 PM'), ('12 PM', '12 PM'), ('4 PM', '4 PM'), ('2 PM', '2 PM'), ('10 AM', '10 AM'), ('8 PM', '8 PM'), ('8 AM', '8 AM')], default='8 AM', max_length=20, verbose_name='Pick a Slot'),
        ),
    ]