
from django.urls import path, re_path, register_converter
from . import views
from . import converters


register_converter(converters.FourDigitYearConverter, "year4")
urlpatterns = [
    path('about/', views.about, name='about'),
    path('women/', views.index, name='women'),
    path('cats/', views.categories, name='cats'),
    path('addpage/', views.addpage, name='add_page'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login, name='login'),
    path('cats/<int:cat_id>/', views.categories_byint, name='cats_int'),
    path('cats/<slug:cat_slug>/', views.categories_byslug, name='cats_slug'),
    path('', views.head, name='home'),
    path('archive/<year4:year>', views.archive, name='arch'),
    path('post/<int:post_id>/', views.show_post, name='post')
]