from django.db import models
from django.utils import timezone

# Create your models here.


class Product(models.Model):
    
    x = [
        ('phone','phone'),
        ('computer','computer'),
    ]
    
    name = models.CharField(max_length=255, verbose_name='Title')
    # name = models.CharField(max_length=255, default='add your name', verbose_name='title')
    content = models.TextField(null=True, blank=True, verbose_name='Description')
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.ImageField(upload_to='photos/%y%m%d', verbose_name='Photo')
    active = models.BooleanField(default=True)
    category = models.CharField(max_length=255,null=True, blank=True, choices=x)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Phone' 
        ordering = ['name']
        # ordering = ['-name']
    

class Test(models.Model):
    date = models.DateField()
    time = models.TimeField(null=True)
    created = models.DateTimeField(default=timezone.now)
    # created = models.DateTimeField(auto_now_add=True)
    