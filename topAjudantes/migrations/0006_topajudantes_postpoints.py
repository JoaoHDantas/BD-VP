# Generated by Django 5.1 on 2024-11-30 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topAjudantes', '0005_rename_fraseefeito_topajudantes_nicknameajudante_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='topajudantes',
            name='postPoints',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]