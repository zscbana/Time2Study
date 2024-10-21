from django.urls import path
from . import views


urlpatterns = [
    path("", views.timer, name="timer"),
    path("status/", views.status, name="status"),
]
