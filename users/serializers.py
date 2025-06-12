from rest_framework import serializers
from .models import Utilisateur, Competence

class CompetenceUtilisateur(serializers.ModelSerializer):
    class Meta:
        model = Competence
        fields = '__all__'
        read_only_fields = ['id']

class UtilisateurSerializer(serializers.ModelSerializer):
    competences = CompetenceUtilisateur(many=True, required=False)
    class Meta :
        model = Utilisateur
        fields = '__all__'
        extra_kwargs = {
            'password':{'write_only':True}
        }
        read_only_fields = ['id','date_creation', 'date_modification']

    def create(self, **validated_data):
        password = validated_data['password']
        user = Utilisateur(**validated_data)
        user.set_password(password)
        user.save()
        return user     