from rest_framework import serializers
from .models import Utilisateur, Competence

class CompetenceUtilisateur(serializers.ModelSerializer):
    class Meta:
        model = Competence
        fields = '__all__'
        read_only_fields = ['id']

class UtilisateurSerializer(serializers.ModelSerializer):
    competences = CompetenceUtilisateur(required=False, many=True)
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = Utilisateur
        fields = [
            'email', 'photo_profil', 'password', 'nom', 'fonctions', 'slogan',
            'nombre_projet', 'nombre_recompense', 'lien_facebook', 'lien_instagram',
            'lien_twitter', 'lien_github', 'biographie', 'competences'
        ]
        extra_kwargs = {
            'password': {'write_only': True}
        }
        read_only_fields = ['id', 'date_creation', 'date_modification']

    def create(self, validated_data):
        competences_data = validated_data.pop('competences', [])
        password = validated_data.pop('password', None)

        if not password:
            raise serializers.ValidationError({"password": "Ce champ est obligatoire."})

        user = Utilisateur(**validated_data)
        user.set_password(password)
        user.save()

        # Associer les compétences
        for comp_data in competences_data:
            comp, _ = Competence.objects.get_or_create(**comp_data)
            user.competences.add(comp)

        return user
