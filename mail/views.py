from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse
from django.core.mail import send_mail

import os

from dotenv import load_dotenv

load_dotenv()

@api_view(['POST'])
def send_email(request):
    data = request.data
    
    name = data.get("name")
    email = data.get("email")
    message = data.get("message")
    
    if not name or not email or not message:
        return HttpResponse(''' <div class="form-response error">
                                    <p>Information is missing! Please try again.</p>
                                </div>''')

    try:
        send_mail(
            f"Website: Inquiry from {name}",
            f"Email: {email}\nmessage",
            os.getenv("SENDER_EMAIL"),
            [os.getenv("RECEIVER_EMAIL", "omivernutrition@gmail.com")],
            fail_silently=False
        )
        return HttpResponse(''' <div class="form-response success">
                                    <p>Thank you! Your email has been sent successfully.</p>
                                </div>''')
    except Exception as e:
        return HttpResponse(f'''<div class="form-response error">
                                    <p>Oops! Something went wrong. Please try again, or email us directly at omivernutrition@gmail.com.</p>
                                </div>''')