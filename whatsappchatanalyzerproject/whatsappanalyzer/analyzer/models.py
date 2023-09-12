from django.db import models

# Create your models here.
from django.db import models
import os

class WhatsAppFile(models.Model):
    uniqueidentifier=models.CharField(max_length=100,null=False)
    file = models.FileField(upload_to='chatfile/',default=False,null=False)
    

     