# Generated by Django 5.1 on 2024-09-15 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userProfile', '0003_userprofile_userpixels'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='fraseEfeito',
            field=models.TextField(blank=True, null=True),
        ),
    ]
