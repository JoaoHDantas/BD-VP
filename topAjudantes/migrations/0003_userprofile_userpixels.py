# Generated by Django 5.1 on 2024-09-14 15:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pixel', '0002_pixel_upload'),
        ('topAjudantes', '0002_userprofile_profile_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='topAjudantes',
            name='userPixels',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pixel.pixel'),
        ),
    ]
