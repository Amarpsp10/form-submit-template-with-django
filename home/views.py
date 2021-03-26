from django.shortcuts import render, HttpResponse

# Create your views here.


def index(request):
    context = {
        'variable': 'there we go :) '
    }
    return render(request, 'myindex.html', context)
    # return HttpResponse("this is home page")


def about(request):
    return HttpResponse("this is about page")
