from django.urls import path
from .views import send_email

urlpatterns = [
    path('email-inquiry', send_email, name='send-email'),
]