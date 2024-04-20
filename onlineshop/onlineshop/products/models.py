from django.db import models

# Create your models here.


class Address(models.Model):
    street = models.CharField(max_length = 100)
    zipcode = models.CharField(max_length = 10)
    city = models.CharField(max_length = 50)
    country = models.CharField(max_length = 50)

    def __str__(self):
        return f"{self.street}, {self.city}, {self.country}"


class Brand(models.Model):
    title = models.CharField(max_length = 70)
    logo = models.ImageField()
    address = models.OneToOneField(Address, on_delete = models.CASCADE,null = True)

    def __str__(self):
        return f"{self.title}"

class Category(models.Model):
    title = models.CharField(max_length = 30)
    description  = models.TextField()
    def __str__(self):
        return f"{self.title}"


class Product(models.Model):
    title = models.CharField(max_length = 70)
    image = models.ImageField(blank=True, upload_to="product-img")
    category = models.ManyToManyField(Category)
    brand = models.ForeignKey(Brand,on_delete = models.CASCADE, null = True, related_name = "product")
    price = models.PositiveIntegerField()
    description = models.TextField()
    slug = models.SlugField(blank = True)
    is_bestseller = models.BooleanField(default = False)
    suggestions = models.ManyToManyField('self')

    def __str__(self):
        return f"{self.title} ${self.price}"
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.slug = self.id
        super().save(*args, **kwargs)