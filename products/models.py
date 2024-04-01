from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=100) 
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.ManyToManyField('Category', null=True, blank=True)
    sku = models.CharField(max_length=254, null=True, blank=True)
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


# From Walkhrough 

class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    is_active = models.BooleanField(default=True)

    subcategories = models.ManyToManyField('self', symmetrical=False)


    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name
