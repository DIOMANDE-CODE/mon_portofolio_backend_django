from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny

from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt

from .serializers import ContactSerializer
from .models import Contact
from django.core.mail import EmailMessage
from django.conf import settings

from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

from django.http import JsonResponse


# Create your views here.

# API POST : Enregistrement d'un contact
@permission_classes([AllowAny])
@api_view(['POST'])
def enregistrement_contact(request):
    serializer = ContactSerializer(data=request.data)
    if serializer.is_valid():
        contact = serializer.save()

        subject = f"Nouveau message de : {contact.nom_client}"
        from_email = "no-reply@tonsite.com"
        to_email = ["chezpyth@gmail.com"]

        context = {
            'nom': contact.nom_client,
            'email': contact.email_client,
            'sujet': contact.service_client,
            'message': contact.message_client,
            'numero_telephone' : contact.numero_client,
            'date_reception': contact.date_reception,
        }

        # Charger le template HTML et texte
        html_content = render_to_string('emails/contact_email.html', context)
        text_content = render_to_string('emails/contact_email.txt', context)

        email = EmailMultiAlternatives(subject, text_content, from_email, to_email)
        email.attach_alternative(html_content, "text/html")
        email.send()


        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def acceuil(request):
    return JsonResponse({
        'message':'Bienvenue sur mon API backend'
    })