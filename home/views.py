from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages

# Create your views here.


def index(request):
    if request.method == "POST":
        mail = request.POST.get('mail')
        name = request.POST.get('name')
        message = request.POST.get('message')
        contact = Contact(mail=mail, name=name,
                          message=message, date=datetime.today())
        contact.save()
        messages.success(request, 'your message has been sent!')
    return render(request, 'myindex.html')
