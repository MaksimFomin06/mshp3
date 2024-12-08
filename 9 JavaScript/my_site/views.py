from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.
def index_page(request: HttpRequest) -> HttpResponse:
    context = {
        "title": "Главная",
    }
    return render(request, "my_site/index.html", context)