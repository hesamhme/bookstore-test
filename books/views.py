from django.shortcuts import render
from django.views import generic
from .models import Books


class BookList(generic.ListView):
    model = Books
    template_name = 'books/booklist.html'
    context_object_name = 'books'


class BookDetail(generic.DetailView):
    template_name = 'books/detalview.html'
    model = Books

