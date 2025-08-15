from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("welcome_page", views.welcome_page, name="welcome_page")
]