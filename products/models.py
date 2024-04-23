from django.db import models
from django.contrib.auth.models import User
from profiles.models import UserProfile

class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'
        
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    is_filterable = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name

class SubCategory(models.Model):
    name = models.CharField(max_length=100)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategories')

    class Meta:
        verbose_name_plural = 'Subcategories'

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    name = models.CharField(max_length=100) 
    description = models.TextField()
    category = models.ManyToManyField(Category, related_name='products', blank=True)
    sub_category = models.ManyToManyField(SubCategory, related_name='products', blank=True)
    sku = models.CharField(max_length=254, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    is_bestseller = models.BooleanField(default=False)
    is_new_items = models.BooleanField(default=False) 
    is_last_chance= models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Wishlist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    product = models.ManyToManyField(Product, related_name='wishlist_products', null=False)
    added_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Wishlist for {self.user.username}'

