from django.db import models

#1 Question contains N Groups
class Question(models.Model):
    name = models.CharField(max_length=50)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

class Group(models.Model):
    name = models.CharField(max_length=255)

#N Participant answear 1 Question
class Participant(models.Model):
    name = models.CharField(max_length=50)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
