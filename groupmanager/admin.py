from django.contrib import admin

# Register your models here.
from .models import Question
admin.site.register(Question)

from .models import Group
admin.site.register(Group)

from .models import Participant
admin.site.register(Participant)
