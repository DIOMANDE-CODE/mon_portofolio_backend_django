from django.urls import path
from .views import creation_utilisateur, liste_des_utilisateurs

urlpatterns = [
    path('create/', creation_utilisateur, name='creation_utilisateur'),
    path('list/', liste_des_utilisateurs, name='liste_des_utilisateurs'),
]
