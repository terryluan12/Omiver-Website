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
        },
        {
            "pk": 3,
            "title": "TITLE 4",
            "email": "4444@yahoo.com",
            "snippet": "44444",
            "description": "This is a full description of ticket 4"
        },
        {
            "pk": 4,
            "title": "TITLE 5",
            "email": "5555@yahoo.com",
            "snippet": "asdfasdfasfdasf",
            "description": "This is a full description of ticket 5"
        },
        {
            "pk": 5,
            "title": "TITLE 6",
            "email": "66666@yahoo.com",
            "snippet": "saddddd",
            "description": "This is a full description of ticket 6"
        }
    ]

def support(request):
    return render(request, "dashboard/support.html", {"tickets": tickets})

def ticket_detail_partial(request, pk):
    ticket = tickets[pk]
    return render(request, "dashboard/ticket_detail_partial.html", ticket)