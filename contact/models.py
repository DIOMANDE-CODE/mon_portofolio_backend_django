from django.db import models
from projets.models import Categorie_Projet
# Create your models here.

class Contact(models.Model):
    nom_client = models.CharField(max_length=200, help_text="Nom et Prenom du client") # Nom et Prenoms du client
    email_client = models.EmailField() # Email du client
    numero_client = models.CharField(max_length=30, help_text="numero du client") # Numero du client
    service_client = models.ForeignKey(Categorie_Projet, on_delete=models.CASCADE, related_name="contacts") # service demandé par le client
    message_client = models.TextField(help_text="message du client") # Message du client

    date_reception = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nom_client