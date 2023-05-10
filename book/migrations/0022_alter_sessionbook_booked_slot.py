# Generated by Django 3.2.18 on 2023-05-09 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0021_alter_sessionbook_booked_slot'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sessionbook',
            name='booked_slot',
            field=models.CharField(choices=[('8 AM', '8 AM'), ('12 PM', '12 PM'), ('2 PM', '2 PM'), ('10 AM', '10 AM'), ('4 PM', '4 PM'), ('8 PM', '8 PM'), ('6 PM', '6 PM')], default='8 AM', max_length=10, verbose_name='Pick a Slot'),
        ),
    ]
