from django.urls import path
from .views import enregistrement_contact

urlpatterns = [
    path('create/', enregistrement_contact, name='enregistrement_contact'),
]
