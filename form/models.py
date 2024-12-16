from django.db import models

class FormModel(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=60)
    num = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

# Create your models here.
