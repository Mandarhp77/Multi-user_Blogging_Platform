from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path("reader/", views.reader, name="reader"),
    path("writer/", views.writer, name="writer"),
    path("writer", views.writer, name="writer"),
    path("user/", views.user, name="user"),
    path("register/", views.register, name="register"),
    path("register", views.register, name="register"),
    path("login/", views.login, name="login"),
    path("search_cat", views.search_cat, name="search_cat"),
    path("search_user", views.search_user, name="search_user"),
    path("login", views.login, name="login"),
    path("blog", views.blog, name="blog"),
    
] 
