from django.db import models

# Create your models here.
class Book(models.Model):
  name = models.CharField(max_length=120)
  auhtor = models.CharField(max_length=120)
  reference = models.CharField(max_length=50)


  def __str__(self):
    return self.name