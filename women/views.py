from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponsePermanentRedirect
from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.views.generic import TemplateView, ListView, DetailView, FormView, CreateView
from django.urls import reverse_lazy

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


# def index(request):
#     data = {'title': "Главная страница приложения women",
#             'menu': menu,
#             'posts': db,
#             'cat_selected': 0,
#             }
#     return render(request, 'women/index.html', context=data)


# def handle_uploaded_file(f):
#     with open(f"upload/{f.name}", "wb+") as destination:
#         for chunk in f.chunks():
#             destination.write(chunk)


def about(request):
    # if request.method == 'POST':
    #     form = FileForm(request.POST, request.FILES)
    #     if form.is_valid():
    #         #handle_uploaded_file(form.cleaned_data['file'])
    #         f = UploadFiles(file=form.cleaned_data['file'])
    #         f.save()
    # else:
    #     form = FileForm()
    return render(request, 'women/about.html',
                  context={'title': "О сайте", 'menu': menu})


def categories(request):
    return HttpResponse("<h1>Главная страница приложения categories</h1>")


# def show_category(request, cat_slug):
#     category = get_object_or_404(Categories, slug=cat_slug)
#     posts = Women.objects.filter(is_publ=1, cat_id=category.pk).select_related('cat')
#     data = {'title': f"Рубрика: {category}",
#             'menu': menu,
#             'posts': posts,
#             'cat_selected': category.pk
#             }
#     return render(request, 'women/index.html', context=data)


class CategoryList(ListView):
    template_name = 'women/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        return Women.objects.filter(is_publ=1, cat__slug=self.kwargs['cat_slug']).select_related('cat')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cat = context['posts'][0].cat
        context['title'] = 'Категория' + cat.name
        context['menu'] = menu
        context['cat_selected'] = cat.pk
        return context

def head(request):
    return render(request, 'women/index.html', {'menu': menu})

def contact(request):
    return render(request, 'women/index.html', {'menu': menu, 'title': 'Список контактов'})

def login(request):
    return render(request, 'women/index.html', {'menu': menu, 'title': 'Авторизация'})


# def show_post(request, post_slug):
#     posts = get_object_or_404(Women, slug=post_slug)
#     data = {'title': posts.name,
#             'menu': menu,
#             'posts': posts,
#             'cat_selected': 1,
#             }
#     return render(request, 'women/post.html', data)

class ShowPostList(DetailView):
    template_name = 'women/post.html'
    context_object_name = 'posts'
    slug_url_kwarg = 'post_slug'

    def get_queryset(self):
        return Women.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['posts'].name
        context['menu'] = menu
        return context

    def get_object(self, queryset=None):
        return get_object_or_404(Women.public, slug=self.kwargs[self.slug_url_kwarg])

class TagList(ListView):
    template_name = 'women/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        return Women.public.filter(tags__slug=self.kwargs['tag_slug']).select_related('cat')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tag = context['posts'][0].tags.all()[0]
        context['title'] = 'Категория' + tag.tag
        context['menu'] = menu
        context['cat_selected'] = tag.pk
        return context




def page_not_found(request, exception):
    return HttpResponseNotFound("Страница не найдена")


class AddPage(FormView):
    form_class = AddPostForm
    template_name = 'women/addpage.html'
    extra_context = {'menu': menu,
                     'title': 'Добавить пост'}
    success_url = reverse_lazy('women')
    #messages.success(request, messages.INFO, "Статья успешно добавлена на сайт!")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class WomenHome(ListView):
    #model = Women
    template_name = 'women/index.html'
    context_object_name = 'posts'
    extra_context = {'title': "Главная страница приложения women",
                     'menu': menu,
                     'posts': db,
                     'cat_selected': 0}



    def get_queryset(self):
        return Women.public.all().select_related('cat')

