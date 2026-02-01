from django.core.management.base import BaseCommand
from projets.models import Categorie_Projet, Visuel, Projet

DEFAULT_IMAGE_URL = "https://res.cloudinary.com/darkqhocp/image/upload/v1769903630/image-informatique_rgwyv3.jpg"

class Command(BaseCommand):
    help = "Remplace toutes les images des catégories, visuels et projets par l'image par défaut Cloudinary"

    def handle(self, *args, **options):
        # Catégories
        for categorie in Categorie_Projet.objects.all():
            categorie.image_categorie = DEFAULT_IMAGE_URL
            categorie.save(update_fields=["image_categorie"])
            self.stdout.write(self.style.SUCCESS(f"Catégorie '{categorie.nom_categorie}' mise à jour."))

        # Visuels
        for visuel in Visuel.objects.all():
            visuel.image_visuel = DEFAULT_IMAGE_URL
            visuel.save(update_fields=["image_visuel"])
            self.stdout.write(self.style.SUCCESS(f"Visuel '{visuel.titre_visuel}' mis à jour."))

        # Projets
        for projet in Projet.objects.all():
            projet.image_projet = DEFAULT_IMAGE_URL
            projet.save(update_fields=["image_projet"])
            self.stdout.write(self.style.SUCCESS(f"Projet '{projet.titre_projet}' mis à jour."))

        self.stdout.write(self.style.SUCCESS("Toutes les images ont été remplacées par l'image par défaut."))
