# Generated by Django 5.2.2 on 2025-06-16 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projets', '0013_alter_categorie_projet_image_categorie_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorie_projet',
            name='image_categorie',
            field=models.ImageField(blank=True, null=True, upload_to='projet/image_categorie/'),
        ),
        migrations.AlterField(
            model_name='projet',
            name='image_projet',
            field=models.ImageField(blank=True, null=True, upload_to='projet/image_projet/'),
        ),
        migrations.AlterField(
            model_name='visuel',
            name='image_visuel',
            field=models.ImageField(upload_to='projet/visuel/'),
        ),
    ]
