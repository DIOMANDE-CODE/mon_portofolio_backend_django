from django.urls import path
from .views import creation_categorie_projet, liste_categorie_projet, liste_des_projets, liste_projet_par_categorie, liste_des_visuels, detail_du_projet

urlpatterns = [
    path('categorie/create/', creation_categorie_projet, name='creation_categorie_projet'),
    path('categorie/list/', liste_categorie_projet, name='liste_categorie_projet'),
    path('categorie/projet/<int:pk>/', liste_projet_par_categorie, name='liste_projet_par_categorie'),

    path('list/', liste_des_projets, name='liste_des_projets'),
    path('detail/<int:pk>/', detail_du_projet, name='detail_du_projet'),

    # Afficher les visuels
    path('visuel/list/', liste_des_visuels, name='liste_des_visuels'),
]
