from django.db import models

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length = 70)
    category = models.CharField(max_length = 50)
    image = models.ImageField(blank=True)
    price = models.PositiveIntegerField()
    brand = models.CharField(max_length = 50)
    description = models.TextField()
    
    def __str__(self):
        return f"{self.title} ${self.price}"

class Shirt(models.Model):
    title = models.CharField(max_length = 70)
    price = models.PositiveIntegerField()
    brand = models.CharField(max_length = 50, null=True)
    description = models.TextField(blank = True)
    is_bestseller = models.BooleanField(default = False)

    def __str__(self):
        return f"{self.title} ${self.price}"