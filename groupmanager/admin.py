from django.contrib import admin

# Register your models here.
from .models import Event
admin.site.register(Event)

from .models import Topic
admin.site.register(Topic)

from .models import Participant
admin.site.register(Participant)
