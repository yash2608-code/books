from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.AddBookPage, name="addbookpage"),
    path('show-books/', views.ShowBookPage, name="showbook"),
    path('add-book/', views.AddBook, name="addbook"),
]
