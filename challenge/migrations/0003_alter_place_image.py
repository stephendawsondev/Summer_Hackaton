# Generated by Django 4.2.3 on 2023-07-14 21:00

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("challenge", "0002_remove_place_updated_on"),
    ]

    operations = [
        migrations.AlterField(
            model_name="place",
            name="image",
            field=cloudinary.models.CloudinaryField(
                default=None, max_length=255, verbose_name="image"
            ),
        ),
    ]
