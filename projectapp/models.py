from django.db import models

# Create your models here.
class Search(models.Model):
    name = models.TextField()
    custom_number = models.TextField()