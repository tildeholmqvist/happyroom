from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Service(models.Model):
    type = models.CharField(max_length=250)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.type


class BookService(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=User.objects.first)
    date_time = models.DateTimeField()
    message = models.TextField()
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.user.username} - {self.service.type} - {self.date_time}"

    class Meta:
        ordering = ['date_time']
