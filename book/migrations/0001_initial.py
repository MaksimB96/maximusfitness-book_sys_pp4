# Generated by Django 3.2.18 on 2023-04-26 18:52

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.DateField(default=datetime.datetime.now)),
                ('time', models.CharField(choices=[('10 AM', '10 AM'), ('6 PM', '6 PM'), ('4 PM', '4 PM'), ('2 PM', '2 PM'), ('12 PM', '12 PM'), ('8 AM', '8 AM')], default='8 AM', max_length=10)),
                ('confirm_status', models.CharField(choices=[('declined', 'declined'), ('pending', 'pending'), ('confirmed', 'confirmed')], default='pending', max_length=10)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]