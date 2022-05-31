from django.db import models

# Create your models here.
class familiar(models.Model):
    name = models.CharField(max_length=30)
    birth = models.DateField()
    age = models.IntegerField()