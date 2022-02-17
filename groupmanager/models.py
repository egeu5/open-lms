from django.db import models

# 1 Event contains N Topics
class Event(models.Model):
    eid = models.IntegerField("event id")  # event ID
    title = models.CharField("event title", max_length=50)
    expert_phase = models.BooleanField("event is in expert phase")  # Phase, in der die Gruppen neu zugeordnet wurden

# 1 Topic contains N Participants
class Topic(models.Model):
    title = models.CharField("topic title", max_length=255)
    event = models.ForeignKey("reference event", Event, on_delete=models.CASCADE)

# N Participants belong to M Topics
class Participant(models.Model):
    name = models.CharField("participant display name", max_length=50)
    topics = models.ManyToManyField("chosen topics", Topic, on_delete=models.CASCADE)
