from statistics import mode
from unicodedata import name
from django.db import models

class Question(models.Model):
    assignment = models.CharField(max_length=50)
    


class Participant(models.Model):
    name = models.CharField(max_length=50)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
