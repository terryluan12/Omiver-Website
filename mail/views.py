from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail
from rest_framework import status

# Create your views here.



@api_view(['POST'])
def send_email(request):
    data = request.data
    
    name = data.get("name")
    email = data.get("email")
    message = data.get("message")
    
    if not name or not email or not message:
        return HttpResponse('<p style="color:red;">Failed to send email. Try again.</p>')

    try:
        send_mail(
            f"Website: Inquiry from {name}",
            f"Email: {email}\nmessage",
            "test-eqvygm0k3yzl0p7w.mlsender.net",
            ["terry.luan@canadianmusicians.coop"],
            fail_silently=False
        )
        return HttpResponse('<p style="color:green;">Email sent successfully!</p>')
    except Exception as e:
        return HttpResponse(f'<p style="color:red;">Something went wrong: {str(e)} Try again.</p>')