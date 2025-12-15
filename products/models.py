from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField()
    description = models.TextField()
    precio = models.IntegerField()
    available = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name    
