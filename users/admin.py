from django.contrib import admin
from .models import Utilisateur, Competence

# Register your models here.

@admin.register(Competence)
class CompetenceAdmin(admin.ModelAdmin):
    list_display = ('nom_competence',)
    search_fields = ('nom_competence',)
    ordering = ['nom_competence']

@admin.register(Utilisateur)
class UtilisateurAdmin(admin.ModelAdmin):
    list_display = ('email', 'nom', 'photo_profil', 'is_active', 'is_superuser',)
    search_fields = ('email','nom',)
    ordering = ['nom']
