from django.contrib import admin
from .models import Categorie_Projet, Technologie, Projet, Visuel

# Register your models here.

@admin.register(Categorie_Projet)
class CategoryProjetAdmin(admin.ModelAdmin):
    list_display = ('nom_categorie', 'image_categorie', 'description_categorie',)
    search_fields = ('nom_categorie',)
    ordering = ['nom_categorie']


@admin.register(Visuel)
class VisuelAdmin(admin.ModelAdmin):
    list_display = ( 'titre_visuel','image_visuel',)
    search_fields = ('titre_visuel',)
    ordering = ['titre_visuel']


@admin.register(Technologie)
class TechnologieAdmin(admin.ModelAdmin):
    list_display = ('nom_technologie',)
    search_fields = ('nom_technologie',)
    ordering = ['nom_technologie']

@admin.register(Projet)
class ProjetAdmin(admin.ModelAdmin):
    list_display = ('titre_projet', 'proprietaire',  'categorie_projet', 'date_debut', 'date_fin',)
    search_fields = ('titre_projet',)
    ordering = ['date_debut']
