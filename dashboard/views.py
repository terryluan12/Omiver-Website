import json
import os
from django.shortcuts import render
from django.conf import settings as django_settings

# Create your views here.

tickets = [
        {
            "pk": 0,
            "title": "Meal Plan Feedback",
            "email": "plans@omiver.me",
            "snippet": "Thank you for reaching out to Omiver...",
            "description": """Hello James,

Thank you for reaching out to Omiver with alternative breakfast meal plan suggestions for Sofia. We have written our feedback regarding your suggestion:

“Your veggie egg scramble recipe will be added to Sofia’s recommended breakfast meal plan. We would suggest adding customization with her favorite vegetables, including spinach, broccoli, mushrooms, peppers. For additional protein, we also recommend adding low-fat cheese. Similarly, she can also use egg whites instead of whole eggs to lower the recipe’s cholesterol levels.”

Your suggestion will be taken into account for future meal plan recommendations. If you have additional feedback regarding your client’s meal plans, please do not hesitate to reach out!

Best Regards,
Meal Planning Team
Omiver
            """
        },
        {
            "pk": 1,
            "title": "Solution for Your Issue - Login Error",
            "email": "support@omiver.me",
            "snippet": "We sincerely apologize for the inconvenience...",
            "description": """Hello James,

We sincerely apologize for the inconvenience caused by the difficulty to login. It seems that the issue you’re experiencing is a common one. You can find a detailed solution in this knowledge base article: faq.omiver.me.

If you need further assistance or the article doesn’t resolve the issue, don’t hesitate to reply to this email.

Best regards,
IT Support Team
Omiver
            """
        },
        {
            "pk": 2,
            "title": "Test Kit #4838 Tracking Information",
            "email": "tracking@omiver.me",
            "snippet": "Great news! Your order for an additional...",
            "description": """Hello James,

Great news! Your order for an additional Omiver Biomarker Test Kit has been shipped and is on its way to you!

Here are the details:
Order Number: #4838
Shipping Method: FedEx
Tracking Number: 0239480239840293
Estimated Delivery Date: 03/11/2025

You can track your order status anytime using the tracking link above. If you have any questions or need assistance, please don’t hesitate to reach out to us.

Thank you for choosing us. We hope you enjoy your purchase and look forward to serving you again!

Best regards,
Tracking Team
Omiver
            """
        },
        {
            "pk": 3,
            "title": "Feature Request Acknowledgement",
            "email": "product@omiver.me",
            "snippet": "Thanks so much for emailing about...",
            "description": """Hello James,

Thanks so much for emailing about performance tracking from health wearables—that’s a great question! While we don’t have a feature like that currently, we are planning on adding something similar to that in the near future. We will make sure that we reach out to you as soon as this feature goes live. 

Thanks again for reaching out about this and sharing your perspective. Emails like this help keep our service fresh and new.

Thanks,
Product Team
Omiver
            """
        },
        {
            "pk": 4,
            "title": "Feature Request Feedback",
            "email": "support@omiver.me",
            "snippet": "Thank you for raising a request for...",
            "description": """Hello James,

Thank you for raising a request for “Apple Watch Performance Tracking” on 02/01/2025. We are happy to tell you that the feature is on our roadmap, and will go live on 04/06/2025. We will inform you as soon as our feature goes live.

Thanks for your feedback, it helps us assist you better!

Thanks,
IT Support Team
Omiver
            """
        }
    ]

def support(request):
    if request.headers.get("HX-Request") == "true":
        return render(request, "dashboard/partials/support.html", {"tickets": tickets})
    return render(request, "dashboard/support.html", {"tickets": tickets})

def ticket_detail_partial(request, pk):
    ticket = tickets[pk]
    return render(request, "dashboard/ticket_detail_partial.html", ticket)

def dashboard(request):
    return render(request, "dashboard/base.html")

def settings(request):
    if request.headers.get("HX-Request") == "true":
        return render(request, "dashboard/partials/settings.html", {"tickets": tickets})
    return render(request, "dashboard/settings.html")

def profile(request, uid):
    DATA_FILE = os.path.join(django_settings.BASE_DIR, "demo", "data", "profiles.json")
    with open(DATA_FILE) as f:
        all_profiles = json.load(f)
    profile_data = all_profiles[uid]
    return render(request, "dashboard/profile.html", profile_data)

def plans(request, uid):
    DATA_FILE = os.path.join(django_settings.BASE_DIR, "demo", "data", "profiles.json")
    with open(DATA_FILE) as f:
        all_profiles = json.load(f)
    profile_data = all_profiles[uid]
    return render(request, "dashboard/plans.html", profile_data)

def clients(request):
    DATA_FILE = os.path.join(django_settings.BASE_DIR, "demo", "data", "profiles.json")
    with open(DATA_FILE) as f:
        all_profiles = json.load(f)
    return render(request, "dashboard/clients.html", {"profiles": all_profiles})