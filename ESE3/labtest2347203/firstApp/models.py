from django.db import models

class User(models.Model):
    Name = models.CharField(max_length=30)
    PhoneNumber = models.CharField(max_length=10)
    WorkHours = models.CharField(max_length=2)
    Gender = models.CharField(max_length=6)
    Address = models.CharField(max_length=50)