from django.db import models

# Create your models here.
# admin site pw = admin123
class Url(models.Model):
    link = models.CharField(max_length=10000)
    uuid = models.CharField(max_length=10)
    
    