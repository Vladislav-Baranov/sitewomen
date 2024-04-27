from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponsePermanentRedirect, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.views.generic import TemplateView, ListView, DetailView, FormView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from sitewomen.utils import DataMixin
from .models import Women, Categories, TagPosts
from django.template.defaultfilters import cut
from django.urls import reverse
from django.template.loader import render_to_string
from django.shortcuts import get_object_or_404
from .forms import AddPostForm
# Create your views here.

db = Women.public.all().select_related('cat')


class CategoryList(DataMixin, ListView):
    template_name = 'women/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        return Women.objects.filter(is_publ=1, cat__slug=self.kwargs['cat_slug']).select_related('cat')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.get_mixin_context(context, title='Категория' + context['posts'][0].cat.name,
                               cat_selected=context['posts'][0].cat.pk)
        return context


def head(request):
    return redirect('women')


def contact(request):
    return redirect('women')


def login(request):
    return redirect('http://127.0.0.1:8000/users/login')


def about(request):
    current_obj_list = list(Women.public.values_list('name', flat=True))
    p = Paginator(current_obj_list, 3)
    page_num = request.GET.get('page')
    page_list_obj = p.get_page(page_num)
    return render(request, 'women/about.html', {'title': 'О сайте', 'page_list_obj': page_list_obj})


class ShowPostList(DataMixin, DetailView):
    template_name = 'women/post.html'
    context_object_name = 'posts'
    slug_url_kwarg = 'post_slug'

    def get_queryset(self):
        return Women.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.get_mixin_context(context, title=context['posts'].name)
        return context

    def get_object(self, queryset=None):
        return get_object_or_404(Women.public, slug=self.kwargs[self.slug_url_kwarg])


class TagList(DataMixin, ListView):
    template_name = 'women/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        return Women.public.filter(tags__slug=self.kwargs['tag_slug']).select_related('cat')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.get_mixin_context(context, title='Категория' + context['posts'][0].tags.all()[0].tag,
                               cat_selected=context['posts'][0].tags.all()[0].pk)
        return context


def page_not_found(request, exception):
    return HttpResponseNotFound("Страница не найдена")


class AddPage(DataMixin, CreateView):
    form_class = AddPostForm
    template_name = 'women/addpage.html'
    success_url = reverse_lazy('women')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.get_mixin_context(context, title='Добавить статью', button_name='Добавить')
        return context


class DeletePage(DataMixin, DeleteView):
    model = Women
    template_name = 'women/addpage.html'
    success_url = reverse_lazy('women')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.get_mixin_context(context, title='Удалить статью', button_name='Удалить')
        return context


class EditPage(DataMixin, UpdateView):
    model = Women
    fields = ['name', 'info', 'slug', 'tags', 'img']
    template_name = 'women/addpage.html'
    success_url = reverse_lazy('women')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.get_mixin_context(context, title='Панель изменения', button_name='Редактировать')
        return context


class WomenHome(DataMixin, ListView):
    template_name = 'women/index.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Women.public.all().select_related('cat')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return self.get_mixin_context(context)

