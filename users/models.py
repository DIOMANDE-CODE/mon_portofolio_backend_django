from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.validators import MinValueValidator
from cloudinary.models import CloudinaryField

# Create your models here.

def default_photo_profil():
    return 'https://res.cloudinary.com/darkqhocp/image/upload/v1769904804/MA_PHOTO_lc1kdj.jpg'

class Competence(models.Model):
    nom_competence = models.CharField(max_length=100)
    def __str__(self):
        return self.nom_competence


class UtilisateurManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):

        if not email :
            raise ValueError("Veuillez inscrire votre adresse E-mail")

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
    email = models.EmailField(unique=True)
    photo_profil = CloudinaryField(
        'photo_profil',
        folder='mes_projets/MonPortofolio/images/profil/',
        default=default_photo_profil,
        blank=True,
        null=True
    )
    nom = models.CharField(max_length=200, default="")
    fonctions = models.TextField(blank=True, null=True, help_text="Ex : Dévéloppeur - Designer - Formateur")
    slogan = models.CharField(max_length=200, blank=True, null=True)
    nombre_projet = models.IntegerField(default=0, validators=[MinValueValidator(0)], null=True, blank=True)
    nombre_recompense = models.IntegerField(default=0, validators=[MinValueValidator(0)], null=True, blank=True)
    lien_facebook = models.URLField(blank=True, null=True)
    lien_instagram = models.URLField(blank=True, null=True)
    lien_linkedin = models.URLField(blank=True, null=True)
    lien_twitter = models.URLField(blank=True, null=True)
    lien_github = models.URLField(blank=True, null=True)
    biographie = models.TextField(null=True, blank=True)
    competences = models.ManyToManyField(Competence, related_name='profils', blank=True)

    date_creation = models.DateTimeField(auto_now_add=True)
    date_modification = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UtilisateurManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        if self.email and str(self.email).strip():
            return str(self.email)
        if self.nom and str(self.nom).strip():
            return str(self.nom)
        if self.pk:
            return f"Utilisateur {self.pk}"
        return "Utilisateur inconnu"


