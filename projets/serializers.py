from rest_framework import serializers
from .models import Categorie_Projet, Projet, Visuel, Technologie
from users.serializers import UtilisateurSerializer

class CategorieProjetSerializer(serializers.ModelSerializer):
    nombre_projets = serializers.IntegerField(read_only=True)
    class Meta :
        model = Categorie_Projet
        fields = '__all__'
        read_only_fields = ['id']

class VisuelSerializer(serializers.ModelSerializer):

    categorie_visuel = CategorieProjetSerializer(required=False, read_only=True)

    class Meta :
        model=Visuel
        fields = '__all__'
        read_only_fields = ['id', 'date_creation']


class TechnologieSerializer(serializers.ModelSerializer):

    class Meta :
        model=Technologie
        fields = '__all__'
        read_only_fields = ['id']


class ProjetSerializer(serializers.ModelSerializer):

    proprietaire = UtilisateurSerializer(required=False, read_only=True)
    categorie_projet = CategorieProjetSerializer(required=False, read_only=True)
    technologie = TechnologieSerializer(required=False,read_only=True, many=True)

    class Meta :
        model=Projet
        fields = '__all__'
        read_only_fields = ['id', 'date_debut', 'date_fin']

    def validate(self, data):
        date_debut = data.get('date_debut')
        date_fin = data.get('date_fin')

        if date_debut and date_fin <= date_debut :
            raise serializers.ValidationError("La date de fin doit être postérieure ou égale à la date de début.")

        return data