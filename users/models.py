from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.validators import MinValueValidator
from cloudinary.models import CloudinaryField

# Create your models here.

class Competence(models.Model):
    nom_competence = models.CharField(max_length=100)

    def __str__(self):
        return self.nom_competence


class UtilisateurManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):

        if not email :
            ValueError("Veuillez inscrire votre adresse E-mail")

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('is_active', True)
        return self.create_user(email, password, **extra_fields)


class Utilisateur(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True) # Email sera utilisé pour la connexion
    photo_profil = CloudinaryField('photo_profil', blank=True, null=True) # Attribut pour ajouter sa photo de profil
    nom = models.CharField(max_length=200, blank=True, null=True) # Nom et Prenom de l'utilisateur
    fonctions = models.TextField(blank=True, null=True, help_text="Ex : Dévéloppeur - Designer - Formateur") # Liste des fonctions de l'Utilisateur
    slogan = models.CharField(max_length=200, blank=True, null=True) # Slogan de l'utilisateur
    nombre_projet = models.IntegerField(default=0, blank=True, null=False, validators=[MinValueValidator(0)]) # Nombre de projets réalisés
    nombre_recompense = models.IntegerField(default=0, blank=True, null=False, validators=[MinValueValidator(0)]) # Nombre de recompenses
    lien_facebook = models.URLField(blank=True, null=True) # Lien facebook
    lien_instagram = models.URLField(blank=True, null=True) # Lien instagram
    lien_linkedin = models.URLField(blank=True, null=True) # Lien linkedIn
    lien_twitter = models.URLField(blank=True, null=True) # Lien Twitter
    lien_github = models.URLField(blank=True, null=True) # Lien github
    biographie = models.TextField(null=True, blank=True) # Ajouter de la biographie
    competences = models.ManyToManyField(Competence, related_name='profils', blank=True) # Donner ses compétences

    date_creation = models.DateTimeField(auto_now_add=True) # Date de création de l'utilisateur
    date_modification = models.DateTimeField(auto_now=True) # Date modification des infos utilisateurs
    is_active = models.BooleanField(default=True) # Possibilité de se connecter
    is_staff = models.BooleanField(default=False) # Accès à la page de d'administration 

    objects = UtilisateurManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email   