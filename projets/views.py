from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate

from .serializers import CategorieProjetSerializer, ProjetSerializer, VisuelSerializer
from .models import Categorie_Projet, Projet, Visuel

from django.db.models import Count
# Create your views here.

# API GET pour lister les categories
@api_view(['GET'])
def liste_categorie_projet(request):
    categories = Categorie_Projet.objects.annotate(nombre_projets=Count('projets'))
    serializer = CategorieProjetSerializer(categories, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

# API POST pour créer une catégorie
@api_view(['POST'])
def creation_categorie_projet(request):
    serializer = CategorieProjetSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response({
        'catégorie' : serializer.errors,
        'message':'catégorie crée avec succès',
        }, status=status.HTTP_400_BAD_REQUEST)

# API GET pour lister les projets
@api_view(['GET'])
def liste_des_projets(request):
    projets = Projet.objects.filter(est_public=True)
    serializer = ProjetSerializer(projets, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

# API GET : avoir la liste des projets en fonction de la categorie
@api_view(['GET'])
def liste_projet_par_categorie(request, pk):

    # Verifier que la categorie existe
    try :
        categorie = Categorie_Projet.objects.get(id=pk)
    except Categorie_Projet.DoesNotExist:
        return Response({
            'message':'cette catégorie est inexistante'
        })
    
    # recupérer les projets selon les catégorie
    try :
        projets = Projet.objects.filter(categorie_projet=pk)
    except Projet.DoesNotExist:
        return Response({
            'message':'Aucun projet existant'
        })
    
    serializer = ProjetSerializer(projets, many=True)
    return Response(serializer.data)

# API GET : Avoir le detail de chaque projet
@api_view(['GET'])
def detail_du_projet(request,pk):
    projet = Projet.objects.get(id=pk)
    serializer = ProjetSerializer(projet)
    return Response(serializer.data)

# api GET : afficher tous les visuels
@api_view(['GET'])
def liste_des_visuels(request):
    visuels = Visuel.objects.all()
    serializer = VisuelSerializer(visuels, many=True)
    return Response(serializer.data)