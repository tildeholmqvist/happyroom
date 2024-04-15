from django.db import models

class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'
        
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

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
    price = models.DecimalField(max_digits=6, decimal_places=2)
    small_price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    medium_price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    large_price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    xlarge_price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    category = models.ManyToManyField(Category, related_name='products', blank=True)
    sub_category = models.ManyToManyField(SubCategory, related_name='products', blank=True)
    sku = models.CharField(max_length=254, null=True, blank=True)
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    is_bestseller = models.BooleanField(default=False)
    is_new_items = models.BooleanField(default=False)
    is_last_chance= models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
    def get_price(self, selected_size=None):
        if selected_size:
            if selected_size == 'small' and self.small_price:
                return self.small_price
            elif selected_size == 'medium' and self.medium_price:
                return self.medium_price
            elif selected_size == 'large' and self.large_price:
                return self.large_price
