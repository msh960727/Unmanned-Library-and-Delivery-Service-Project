from django.shortcuts import render, get_object_or_404
from .models import Book
from cart.forms import CartAddBookForm
from django.contrib.auth.models import User


def book_list(request):
    books = Book.objects.filter(available=True)
    return render(request, 'library/books/list.html', {'books': books})


def book_detail(request, id, slug):
    book = get_object_or_404(Book, id=id, slug=slug, available=True)
    cart_book_form = CartAddBookForm()
    return render(request,
                  'library/books/detail.html',
                  {'book': book,
                   'cart_book_form': cart_book_form})
