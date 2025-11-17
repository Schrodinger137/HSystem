from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField()
    description = models.TextField()
    precio = models.IntegerField()
    available = models.BooleanField()
    
    def __str__(self):
        return self.name    
