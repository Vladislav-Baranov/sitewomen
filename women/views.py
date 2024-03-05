from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponsePermanentRedirect
from django.shortcuts import render, redirect
from .models import Women, Categories
from django.template.defaultfilters import cut
from django.urls import reverse
from django.template.loader import render_to_string
from django.shortcuts import get_object_or_404
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
db = Women.public.all()


def index(request):
    data = {'title': "Главная страница приложения women",
            'menu': menu,
            'post': db,
            'cat_selected': 1,
            }
    return render(request, 'women/index.html', context=data)


def about(request):
    return render(request, 'women/about.html',
                  context={'title': "О сайте", 'menu': menu})


def categories(request):
    return HttpResponse("<h1>Главная страница приложения categories</h1>")


def show_category(request, cat_slug):
    category = get_object_or_404(Categories, slug=cat_slug)
    posts = Women.objects.filter(is_publ=1, cat_id=category.pk)
    data = {'title': f"Рубрика: {category}",
            'menu': menu,
            'db': posts,
            'cat_selected': category.pk
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


def show_post(request, post_slug):
    posts = get_object_or_404(Women, slug=post_slug)
    data = {'title': posts.name,
            'menu': menu,
            'posts': posts,
            'cat_selected': 1,
            }
    return render(request, 'women/post.html', data)


def page_not_found(request, exception):
    return HttpResponseNotFound("Страница не найдена")
