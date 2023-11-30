from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponsePermanentRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.template.loader import render_to_string
# Create your views here.


def index(request):
    s = render_to_string('index.html')
    return HttpResponse(s)


def categories(request):
    return HttpResponse("<h1>Главная страница приложения categories</h1>")


def categories_byint(request, cat_id):
    return HttpResponse(f"<h1>Страница приложения categories</h1><p>id = {cat_id}")


def categories_byslug(request, cat_slug):
    print(request.GET)
    return HttpResponse(f"<h1>Страница приложения categories</h1><p>id = {cat_slug}")


def head(request):
    return HttpResponse("Главная страница")


def archive(request, year):
    if 1980 <= year <= 2023:
        return HttpResponse(f"Показан архив за {year} год")
    else:
        uri = reverse('cats/')
        return redirect(categories)


def page_not_found(request, exception):
    return HttpResponseNotFound("Страница не найдена")
