from django.db import models

# Create your models here.
class Moto(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=150)
    phone = models.CharField(max_length=30)
    email = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name    