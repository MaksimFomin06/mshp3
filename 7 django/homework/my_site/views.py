from django.http import HttpResponse, HttpRequest
from django.shortcuts import render

# Create your views here.

def index_page(request: HttpRequest) -> HttpResponse:
    from datetime import date
    context: dict = {
        "title": "Главная",
        "lesson_num": "7",
        "theme": "Шаблоны: Автоматизация, наследование, CSS, формы",
        "date": date.today()
    }
    return render(request, "my_site/index.html", context)

def riddle(request: HttpRequest) -> HttpResponse:
    context: dict = {
        "tittle": "Загадка"
    }
    return render(request, "my_site/riddle.html", context)

def answer(request: HttpRequest) -> HttpResponse:
    context: dict = {
        "tittle": "Загадка"
    }
    return render(request, "my_site/answer.html", context)

def multiply(request: HttpRequest) -> HttpResponse:
    context: dict = {
        "tittle": "Таблица умножения",
        "results": []
    }
    for i in range(1, 11):
        result = f'{i} * 5 = {i * 5}'
        context['results'].append(result)
    
    return render(request, "my_site/multiply.html", context)