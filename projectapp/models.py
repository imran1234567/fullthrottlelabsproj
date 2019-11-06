from django.db import models

# Create your models here.
class Search(models.Model):
    name = models.CharField(max_length=140)
    custom_number = models.CharField(max_length=140)


    def __str__(self):
        return str(self.name)
    