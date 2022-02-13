from django.urls import path
from . import views

urlpatterns = [
    path("",views.index, name="index"),
    path("index",views.index, name="index"),
    path("logout",views.logout_request,name="logout")
]