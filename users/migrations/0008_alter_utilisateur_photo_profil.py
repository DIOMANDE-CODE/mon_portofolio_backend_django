# Generated by Django 5.2.2 on 2025-06-16 04:05

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_alter_utilisateur_competences'),
    ]

    operations = [
        migrations.AlterField(
            model_name='utilisateur',
            name='photo_profil',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='photo_profil/'),
        ),
    ]
