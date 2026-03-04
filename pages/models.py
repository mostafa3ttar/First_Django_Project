from django.db import models

# Create your models here.

class Car(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=3)
