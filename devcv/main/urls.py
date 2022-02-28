from django.urls import path
from . import views
from django.contrib.auth.models import User
urlpatterns = [
    path("<str:user>", views.username, name="username"),
    path("",views.index, name="index"),
]
