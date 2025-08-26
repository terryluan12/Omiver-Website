from django.shortcuts import render

# Create your views here.

tickets = [
        {
            "pk": 0,
            "title": "title 1",
            "email": "test@gmail.com",
            "snippet": "test test blah blah blah",
            "description": "This is a full description of ticket 1"
        },
        {
            "pk": 1,
            "title": "title 2",
            "email": "test2@gmail.com",
            "snippet": "test 2test blah blah blah",
            "description": "This is a full description of ticket 2"
        },
        {
            "pk": 2,
            "title": "TITLE 3",
            "email": "test3@yahoo.com",
            "snippet": "333333",
            "description": "This is a full description of ticket 3"
        }
    ]

def support(request):
    return render(request, "dashboard/support.html", {"tickets": tickets})

def ticket_detail_partial(request, pk):
    ticket = tickets[pk]
    return render(request, "dashboard/ticket_detail_partial.html", ticket)