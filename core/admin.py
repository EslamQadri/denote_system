from django.contrib import admin

# Register your models here.
from .models import Send_message,Denote_informations
admin.site.register(Send_message)
admin.site.register(Denote_informations)
