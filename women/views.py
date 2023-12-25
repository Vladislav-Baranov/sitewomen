from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponsePermanentRedirect
from django.shortcuts import render, redirect
from django.template.defaultfilters import cut
from django.urls import reverse
from django.template.loader import render_to_string
# Create your views here.


def index(request):
    data = {'title': "Главная страница приложения women", 'float': 34.56,
            'menu': ["На главную", "Войти", "Обратная связь", "О нас"]}
    return render(request, 'women/index.html', context=data)

def about(request):
    return render(request, 'women/about.html',
                  context={'title': "О сайте", 'info': "Данный сайт содержит информацию о женщинах"})


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
    return redirect(categories)

def page_not_found(request, exception):
    return HttpResponseNotFound("Страница не найдена")
