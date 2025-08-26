from django.urls import path

from . import views

urlpatterns = [
    path("support", views.support, name="select_page"),
    path("ticket_detail_partial/<int:pk>", views.ticket_detail_partial, name="ticket_detail_partial")
]