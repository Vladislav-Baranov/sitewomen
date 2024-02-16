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

cats_db = [
    {'id': 1, 'name': 'Актриссы'},
    {'id': 2, 'name': 'Певицы'},
    {'id': 3, 'name': 'Спортсменки'}
]
db = Women.objects.filter(is_publ=1)


def index(request):
    data = {'title': "Главная страница приложения women", 'float': 34.56,
            'menu': menu,
            'db': db,
            'cat_selected': 0,
            }
    return render(request, 'women/index.html', context=data)


def about(request):
    return render(request, 'women/about.html',
                  context={'title': "О сайте", 'menu': menu})


def categories(request):
    return HttpResponse("<h1>Главная страница приложения categories</h1>")


def show_category(request, cat_id):
    data = {'title': "Главная страница приложения women", 'float': 34.56,
            'menu': menu,
            'db': db,
            'cat_selected': cat_id,
            }
    return render(request, 'women/index.html', context=data)


def head(request):
    return render(request, 'women/index.html', {'menu': menu})


def addpage(request):
    return render(request, 'women/index.html', {'menu': menu, 'title': 'Добавить страницу'})


def contact(request):
    return render(request, 'women/index.html', {'menu': menu, 'title': 'Список контактов'})


def login(request):
    return render(request, 'women/index.html', {'menu': menu, 'title': 'Авторизация'})


def show_post(request, post_id):
    return render(request, 'women/post.html', {'menu': menu, 'db': db, 'title': f'Пост {post_id}', 'post_id': post_id})


def page_not_found(request, exception):
    return HttpResponseNotFound("Страница не найдена")
