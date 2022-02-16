from django.db import models

# 1 Event contains N Topics
class Event(models.Model):
    title = models.CharField(max_length=50)

# 1 Topic contains N Participants
class Topic(models.Model):
    title = models.CharField(max_length=255)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

# N Participants belong to M Topics
class Participant(models.Model):
    name = models.CharField(max_length=50)
    topics = models.ManyToManyField("", Topic, on_delete=models.CASCADE)
