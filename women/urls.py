
from django.urls import path, re_path, register_converter
from . import views
from . import converters


register_converter(converters.FourDigitYearConverter, "year4")
urlpatterns = [
    path('about/', views.about, name='about'),
    path('women/', views.index, name='home'),
    path('cats/', views.categories, name='cats'),
    path('cats/<int:cat_id>/', views.categories_byint, name='cats_int'),
    path('cats/<slug:cat_slug>/', views.categories_byslug, name='cats_slug'),
    path('', views.head, name='head'),
    path('archive/<year4:year>', views.archive, name='arch')
]