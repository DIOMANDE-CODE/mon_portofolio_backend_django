from django.contrib import admin
from .models import Contact

# Register your models here.
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ( 'nom_client', 'email_client', 'numero_client', 'service_client', 'message_client','date_reception',)
    search_fields = ('nom_client',)
    ordering = ['date_reception']