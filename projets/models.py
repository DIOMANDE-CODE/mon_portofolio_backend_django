from django.db import models
from users.models import Utilisateur
from cloudinary.models import CloudinaryField
from django.core.exceptions import ValidationError
# Create your models here.



def default_image_projet():
    return 'https://res.cloudinary.com/darkqhocp/image/upload/v1769903630/image-informatique_rgwyv3.jpg'

class Categorie_Projet(models.Model):
    nom_categorie = models.CharField(max_length=100) # nom de la categorie
    image_categorie = CloudinaryField('image_categorie',folder='mes_projets/MonPortofolio/images/categorie/', default=default_image_projet, null=True, blank=True) # nom de la categorie
    description_categorie = models.TextField(null=True, blank=True) # description du projet

    def __str__(self):
        return self.nom_categorie
    

class Technologie(models.Model):
    nom_technologie = models.CharField(max_length=100, help_text='nom des technologies/logiciels utilisés')

    def __str__(self):
        return self.nom_technologie
    
class Visuel(models.Model):
    proprietaire = models.ForeignKey(Utilisateur, null=True, on_delete=models.CASCADE, related_name='visuels')
    categorie_visuel = models.ForeignKey(Categorie_Projet, on_delete=models.CASCADE, related_name='visuels') # Catgegorie de l'image
    titre_visuel = models.CharField(max_length=200, null=True) # Titre du visuel
    image_visuel = CloudinaryField('image_visuel', folder='mes_projets/MonPortofolio/images/visuels/', default=default_image_projet) # fichier de l'image
    description_visuel = models.TextField(null=True, blank=True) # Description Visuel

    date_creation = models.DateField(auto_now=True) # Date de creation

    def __str__(self):
        return self.titre_visuel

class Projet(models.Model):
    proprietaire = models.ForeignKey(Utilisateur, null=True, on_delete=models.CASCADE, related_name='projets')
    titre_projet = models.CharField(max_length=200) # Titre du projet
    description_projet = models.TextField(blank=True, null=True) # description du projet
    categorie_projet = models.ForeignKey(Categorie_Projet, on_delete=models.CASCADE, related_name='projets', blank=True, null=True) # categorie du projet
    technologie = models.ManyToManyField(Technologie, blank=True, help_text='technologies/logiciels utilisés') # Technologie utilisée
    image_projet = CloudinaryField('image_projet', folder='mes_projets/MonPortofolio/images/projets/', default=default_image_projet, blank=True, null=True) # image du projet

    lien_drive = models.URLField(blank=True, null=True, help_text='lien drive du projet') # lien drive du projet
    lien_facebook = models.URLField(blank=True, null=True, help_text='lien facebook du projet') # lien facebook du projet
    lien_instagram = models.URLField(blank=True, null=True, help_text='lien instagram du projet') # lien du projet
    lien_github = models.URLField(blank=True, null=True, help_text='lien github du projet') # lien github du projet
    lien_projet = models.URLField(blank=True, null=True, help_text='lien du projet (web, mobile)') # lien du projet


    date_debut = models.DateField(null=True, blank=True, help_text='date de debut du projet')
    date_fin = models.DateField(null=True, blank=True, help_text='date de fin du projet')
    est_public = models.BooleanField(default=True, help_text="Permettre aux visiteurs de voir le projet")

    date_creation = models.DateTimeField(auto_now_add=True)
    date_modification = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return self.titre_projet
    
    def clean(self):
        super().clean()
        if self.date_fin and self.date_fin < self.date_debut:
            raise ValidationError("La date de fin doit être postérieure ou égale à la date de début.")