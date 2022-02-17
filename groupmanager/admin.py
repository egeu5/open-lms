from django.contrib import admin
from .models import *

# registriere models
admin.site.register(Event)
admin.site.register(Topic)
admin.site.register(Participant)
