from django.urls import path

from . import views

urlpatterns = [
    path("", views.index_page, name="demo_page"),
    path("welcome", views.welcome_page, name="welcome_default_page"),
    path("welcome/<slug:index>", views.welcome_page, name="welcome_page"),
    path("select", views.select_page, name="select_page"),
    path("profile_detail/<int:id>", views.profile_detail, name="profile_detail_page"),
    path("process", views.process, name="process_page"),
    path("layout", views.layout, name="layout_page"),
]
