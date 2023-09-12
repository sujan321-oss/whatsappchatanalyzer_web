from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import WhatsAppFile


class ChatFile(admin.ModelAdmin):
    list_display=("id","uniqueidentifier",'file')
    


admin.site.register(WhatsAppFile,ChatFile)  


