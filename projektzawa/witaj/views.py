from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime

def hello(request):
    return HttpResponse("Witaj w Django!")

def hello_name(request, name):
    return HttpResponse(f"Witaj, {name}!")

def hello_template(request, name):
    return render(request, "witaj/hello.html", {"name": name})

def current_time(request):
    now = datetime.now()
    date_str = now.strftime("%d.%m.%Y")
    time_str = now.strftime("%H:%M")

    context = {
        'date': date_str,
        'time': time_str,
    }
    return render(request, 'witaj/time.html', context)
