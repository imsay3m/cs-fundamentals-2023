# Generated by Django 5.0.1 on 2024-01-12 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carlistings', '0003_remove_car_buyer_car_buyer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='description',
            field=models.TextField(max_length=335),
        ),
    ]
