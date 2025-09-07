from django.urls import path

from . import views

urlpatterns = [
    path("support", views.support, name="support_page"),
    path("ticket_detail_partial/<int:pk>", views.ticket_detail_partial, name="ticket_detail_partial"),
    path("", views.dashboard, name="dashboard_base"),
    path("settings", views.settings, name="settings_page"),
    path("plans/<int:uid>", views.plans, name="plans_page"),
    path("profile/<int:uid>", views.profile, name="profile_page"),
    path("clients", views.clients, name="clients_page")
]