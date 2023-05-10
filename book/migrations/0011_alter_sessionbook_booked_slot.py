# Generated by Django 3.2.18 on 2023-05-07 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0010_auto_20230507_1212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sessionbook',
            name='booked_slot',
            field=models.CharField(choices=[('8 AM', '8 AM'), ('4 PM', '4 PM'), ('8 PM', '8 PM'), ('6 PM', '6 PM'), ('10 AM', '10 AM'), ('2 PM', '2 PM'), ('12 PM', '12 PM')], default='8 AM', max_length=10),
        ),
    ]