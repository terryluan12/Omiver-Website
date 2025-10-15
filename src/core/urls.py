from django.urls import path

from . import views

urlpatterns = [
    path("", views.index_page, name="index_page"),
    path("information", views.information_page, name="information_page"),
    path("login", views.login_page, name="login_page"),
]