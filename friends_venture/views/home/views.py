from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    data = [
        {'name': 'Ema', 'age': 24},
        {'name': 'Zaman', 'age': 30},
        {'name': 'Jakaria', 'age': 31}
    ]
    return render(request, 'index.html', context={'users': data})
    # return HttpResponse("this is the home page")
