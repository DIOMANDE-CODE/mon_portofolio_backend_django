# Generated by Django 5.2.2 on 2025-06-06 01:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projets', '0003_categorie_projet_proprietaire_projet_proprietaire'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categorie_projet',
            name='proprietaire',
        ),
    ]
