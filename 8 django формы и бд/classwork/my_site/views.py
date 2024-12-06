from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from my_site.models import CalculatorDB
# Create your views here.
def index_page(request: HttpRequest) -> HttpResponse:
    context: dict = {
        "title": "Главная"
    }
    if request.method == "POST":
        number_one: int = int(request.POST.get("numberOneName", 0))
        number_two: int = int(request.POST.get("numberTwoName", 0))
        number_ans: int = number_two + number_one
        CalculatorDB(number_one=number_one, number_two=number_two, number_ans=number_ans).save()

    context["data"] = CalculatorDB.objects.all()
    return render(request, "my_site/index.html", context)