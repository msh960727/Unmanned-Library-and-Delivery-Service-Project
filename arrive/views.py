from django.shortcuts import render, get_object_or_404
from .models import ArriveBook
from django.contrib.auth.models import User


def arrive_book_list(request):
    books = ArriveBook.objects.filter(available=True)
    return render(request, 'arrive/arrive_books/list.html', {'books': books})

