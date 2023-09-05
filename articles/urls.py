from django.shortcuts import render, redirect
from django.urls import path
from . import views

urlpatterns = [
    path('', views.article, name='home'),
    path('category/', views.category, name='category'),
    path('category/<slug:category_slug>/', views.article_by_category, name='article_by_category'),
    path('category/<slug:category_slug>/<slug:article_slug>/', views.article_details , name='article_detail'),
]
