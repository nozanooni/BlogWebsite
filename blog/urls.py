
from django.contrib import admin

from django.urls import path
from . import views
from .models import User, Post, Comment, Category


urlpatterns = [
    path('', views.main, name='main'),
    path('master/', views.master, name='master'),
    path('users/', views.users, name='users'),
    path('blogs/', views.blogs, name='blogs'),
    path('comments/', views.comments, name='comments'),
    path('categories/', views.categories, name='categories'),
    path('blogdetails/<int:post_id>/', views.blogdetails, name='blogdetails'),
]

