from django.urls import path

from . import views

app_name = "groupmanager"
urlpatterns = [
    path('', views.index, name='index'),
]