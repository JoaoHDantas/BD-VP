# Generated by Django 5.1 on 2024-11-30 17:25

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topAjudantes', '0004_alter_userprofile_fraseefeito'),
    ]

    operations = [
        migrations.RenameField(
            model_name='topajudantes',
            old_name='fraseEfeito',
            new_name='nicknameAjudante',
        ),
        migrations.AddField(
            model_name='topajudantes',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='topajudantes',
            name='deleted_at',
            field=models.DateTimeField(blank=True, editable=False, null=True),
        ),
        migrations.AddField(
            model_name='topajudantes',
            name='is_active',
            field=models.BooleanField(default=True, editable=False),
        ),
        migrations.AddField(
            model_name='topajudantes',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
