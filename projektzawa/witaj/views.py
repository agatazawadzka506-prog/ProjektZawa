from django.http import HttpResponse
from django.shortcuts import render

# widok podstawowy
def hello(request):
    return HttpResponse("Witaj w Django!")

# widok dynamiczny z imieniem
def hello_name(request, name):
    return HttpResponse(f"Witaj, {name}!")

# widok ze szablonem
def hello_template(request, name):
    return render(request, "witaj/hello.html", {"name": name})
