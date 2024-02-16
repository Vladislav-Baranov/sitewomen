
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
    path('cats/<int:cat_id>/', views.show_category, name='category'),
    path('', views.head, name='home'),
    path('post/<int:post_id>/', views.show_post, name='post')
]