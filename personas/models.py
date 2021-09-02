from django.db import models

# Create your models here.
class Persona(models.Model):
    label = models.CharField(max_length=30)
    slug = models.SlugField(max_length=30)
    info = models.CharField(max_length=90)
    economics = models.PositiveSmallIntegerField()
    date = models.DateTimeField(auto_now_add=True)