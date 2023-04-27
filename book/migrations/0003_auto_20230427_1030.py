# Generated by Django 3.2.18 on 2023-04-27 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_auto_20230427_1026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='confirm_status',
            field=models.CharField(choices=[('pending', 'pending'), ('declined', 'declined'), ('confirmed', 'confirmed')], default='pending', max_length=10),
        ),
        migrations.AlterField(
            model_name='booking',
            name='service',
            field=models.CharField(choices=[('PT Package', 'PT Package'), ('Consultation', 'Consultation'), ('One on One', 'One on One')], default='One on One', max_length=50),
        ),
        migrations.AlterField(
            model_name='booking',
            name='time',
            field=models.CharField(choices=[('10 AM', '10 AM'), ('6 PM', '6 PM'), ('4 PM', '4 PM'), ('8 PM', '8 PM'), ('2 PM', '2 PM'), ('8 AM', '8 AM'), ('12 PM', '12 PM')], default='8 AM', max_length=10),
        ),
    ]