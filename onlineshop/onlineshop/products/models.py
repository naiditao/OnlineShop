from django.db import models

# Create your models here.

class Shirt(models.Model):
    title = models.CharField(max_length = 70)
    price = models.PositiveIntegerField()