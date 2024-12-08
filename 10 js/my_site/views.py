from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render
from django.db.models import QuerySet

from my_site.models import NotesModel


def index(request: HttpRequest) -> HttpResponse:
    context: dict[str, str | QuerySet] = {"page_title": "Главная"}

    if request.method == "POST":
        note_text: str = request.POST.get("noteText", "")
        NotesModel(note_text=note_text).save()

    return render(request, "my_site/index.html", context)


def get_all_notes(request: HttpRequest) -> JsonResponse:
    if request.method == "GET":
        return JsonResponse({"notes": [data.note_text for data in NotesModel.objects.all()]})
    return JsonResponse({"text": "Неправильный тип запроса!"})
