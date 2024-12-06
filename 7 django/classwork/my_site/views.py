from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.

def index_page(request: HttpRequest) -> HttpResponse:
    return render(request, "my_site/index.html")

def time_page(request: HttpRequest) -> HttpResponse:
    from datetime import date
    import time 
    context = {
        "date": date.today(),
        "time": time.strftime("%H:%M:%S",time.localtime()),
    }
    return render(request, "my_site/time.html", context)

def third_page(request: HttpRequest) -> HttpResponse:
    return render(request, "my_site/third.html")