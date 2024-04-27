from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path('login/', views.UsersLogin, name='login'),
    path('logout/', views.UsersLogout, name='logout'),
]
