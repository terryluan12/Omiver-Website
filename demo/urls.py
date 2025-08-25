from django.urls import path

from . import views

urlpatterns = [
    path("select", views.select_page, name="select_page"),
    path("profile_detail/<int:id>", views.profile_detail, name="profile_detail_page"),
    path("process", views.process, name="process_page")
]