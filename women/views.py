from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponsePermanentRedirect
from django.shortcuts import render, redirect
from .models import Women, Categories, TagPosts
from django.template.defaultfilters import cut
from django.urls import reverse
from django.template.loader import render_to_string
from django.shortcuts import get_object_or_404
from .forms import AddPostForm
# Create your views here.

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'}
]


db = Women.public.all().select_related('cat')


def index(request):
    data = {'title': "Главная страница приложения women",
            'menu': menu,
            'posts': db,
            'cat_selected': 0,
            }
    return render(request, 'women/index.html', context=data)


def about(request):
    return render(request, 'women/about.html',
                  context={'title': "О сайте", 'menu': menu})


def categories(request):
    return HttpResponse("<h1>Главная страница приложения categories</h1>")


def show_category(request, cat_slug):
    category = get_object_or_404(Categories, slug=cat_slug)
    posts = Women.objects.filter(is_publ=1, cat_id=category.pk).select_related('cat')
    data = {'title': f"Рубрика: {category}",
            'menu': menu,
            'posts': posts,
            'cat_selected': category.pk
            }
    return render(request, 'women/index.html', context=data)


def head(request):
    return render(request, 'women/index.html', {'menu': menu})


def addpage(request):
    if request.method == 'POST':
         form = AddPostForm(request.POST)
         if form.is_valid():
    #         # print(form.cleaned_data)
    #         try:
    #             if 'tags' in form.cleaned_data.keys():
    #                 t = form.cleaned_data['tags']
    #                 form.cleaned_data.pop('tags', None)
    #                 w = Women.objects.create(**form.cleaned_data)
    #                 w.tags.set(t)
    #             else:
    #                 Women.objects.create(**form.cleaned_data)
    #             return redirect('home')
    #
    #         except:
    #             form.add_error(None, 'Ошибка добавления поста')
            form.save()
            return redirect('home')
    else:
        form = AddPostForm()

    data = {
        'menu': menu,
        'title': 'Добавить пост',
        'form': form
    }

    return render(request, 'women/addpage.html', context=data)


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


def show_tag(request, tag_slug):
    tag = get_object_or_404(TagPosts, slug=tag_slug)
    posts = tag.tags.filter(is_publ=Women.Status.PUBLISHED).select_related('cat')
    data = {'title': f'Тэг: {tag.tag}',
            'menu': menu,
            'posts': posts,
            'cat_selected': None,
            }
    return render(request, 'women/index.html', context=data)


def page_not_found(request, exception):
    return HttpResponseNotFound("Страница не найдена")
