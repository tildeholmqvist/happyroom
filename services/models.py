from django.db import models

# Create your models here.
class ExpertAppointment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    date_time = models.DateTimeField()
    message = models.TextField()
