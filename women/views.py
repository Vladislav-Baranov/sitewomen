from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponsePermanentRedirect
from django.shortcuts import render, redirect
from .models import Women
from django.template.defaultfilters import cut
from django.urls import reverse
from django.template.loader import render_to_string
# Create your views here.

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'}
]

db = Women.objects.filter(is_publ=1)


def index(request):
    data = {'title': "Главная страница приложения women", 'float': 34.56,
            'menu': menu,
            'db': db
            }
    return render(request, 'women/index.html', context=data)


def about(request):
    return render(request, 'women/about.html',
                  context={'title': "О сайте", 'menu': menu})


def categories(request):
    return HttpResponse("<h1>Главная страница приложения categories</h1>")


def categories_byint(request, cat_id):
    return HttpResponse(f"<h1>Страница приложения categories</h1><p>id = {cat_id}")


def categories_byslug(request, cat_slug):
    print(request.GET)
    return HttpResponse(f"<h1>Страница приложения categories</h1><p>id = {cat_slug}")


def head(request):
    return render(request, 'women/index.html', {'menu': menu})


def addpage(request):
    return render(request, 'women/index.html', {'menu': menu, 'title': 'Добавить страницу'})


def contact(request):
    return render(request, 'women/index.html', {'menu': menu, 'title': 'Список контактов'})


def login(request):
    render(request, 'women/index.html', {'menu': menu, 'title': 'Авторизация'})


def archive(request, year):
    if 1980 <= year <= 2023:
        return HttpResponse(f"Показан архив за {year} год")
    return redirect(categories)


def show_post(request, post_id):
    return HttpResponse(f"Показан пост номер {post_id}")


def page_not_found(request, exception):
    return HttpResponseNotFound("Страница не найдена")
