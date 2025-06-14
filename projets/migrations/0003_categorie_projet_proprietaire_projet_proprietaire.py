# Generated by Django 5.2.2 on 2025-06-06 00:59

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projets', '0002_technologie_projet'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='categorie_projet',
            name='proprietaire',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='categories', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='projet',
            name='proprietaire',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='projets', to=settings.AUTH_USER_MODEL),
        ),
    ]
