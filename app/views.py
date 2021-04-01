from django.shortcuts import render, redirect
from .models import *
# Create your views here.


def AddBookPage(request):
    return render(request, "app/addbook.html")


def ShowBookPage(request):
    book = Book.objects.all()
    for i in book:
        print(f"http://127.0.0.1:8000{i.book_file.url}")
    return render(request, "app/showbook.html", {'book': book})


def AddBook(request):
    if request.method == "POST":
        bookn = request.POST['bookn']
        authorn = request.POST['authorn']
        bookp = request.POST['bookp']
        bookf = request.FILES['bookf']

        addbooks = Book.objects.create(
            bookn=bookn, authorn=authorn, bookp=bookp, book_file=bookf)
        return redirect('showbook')
