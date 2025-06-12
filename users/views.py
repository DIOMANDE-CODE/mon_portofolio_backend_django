from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate

from .serializers import UtilisateurSerializer
from .models import Utilisateur

# Create your views here.

# API DE CREATION D'UN UTILISATEUR
@api_view(['POST'])
def creation_utilisateur(request):
    serializer = UtilisateurSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({
            'message':'utilisateur crée avec succès',
            'utilisateur':serializer.data
        }, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# API POUR AFFICHER L'ENSEMBLE DES UTILISATEUR
@api_view(['GET'])
def liste_des_utilisateurs(request):
    utilisateurs = Utilisateur.objects.filter(is_superuser=False)
    serializer = UtilisateurSerializer(utilisateurs, many=True)
    return Response(serializer.data)