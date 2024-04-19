from django.conf.urls.static import static
from django.urls import path, re_path, register_converter, include

from sitewomen import settings
from . import views
from . import converters


register_converter(converters.FourDigitYearConverter, "year4")
urlpatterns = [
    path('about/', views.about, name='about'),
    path('women/', views.WomenHome.as_view(), name='women'),
    path('cats/', views.categories, name='cats'),
    path('addpage/', views.AddPage.as_view(), name='add_page'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login, name='login'),
    path('cats/<slug:cat_slug>/', views.CategoryList.as_view(), name='category'),
    path('', views.head, name='home'),
    path('post/<slug:post_slug>/', views.ShowPostList.as_view(), name='post'),
    path('tag/<slug:tag_slug>/', views.TagList.as_view(), name='tag'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)