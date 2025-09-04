from django.urls import path

from . import views

urlpatterns = [
    path("support", views.support, name="support_page"),
    path("ticket_detail_partial/<int:pk>", views.ticket_detail_partial, name="ticket_detail_partial"),
    path("settings", views.settings, name="settings_page"),
    path("", views.dashboard, name="dashboard_base"),
    path("<str:page_name>", views.dynamic_page, name="dynamic_page")
]