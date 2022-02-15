from django.db import models

# Create your models here.
class Answear(models.Model):
    tID = models.IntegerField()
    aID = models.IntegerField()
    username = models.TextField()