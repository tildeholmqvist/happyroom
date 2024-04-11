from django.db import models

# Create your models here.
class Review(models.Model):
    name = models.CharField(max_length=100)
    comment = models.TextField()

    def __str__(self):
        return self.name