from rest_framework import serializers
from .models import Contact
from projets.serializers import CategorieProjetSerializer


class ContactSerializer(serializers.ModelSerializer):

    class Meta :
        model=Contact
        fields = '__all__'
        read_only_fields = ['id', 'date_reception']