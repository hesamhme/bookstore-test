from django.views import generic
from django.urls import reverse_lazy
from .models import Books


class BookList(generic.ListView):
    model = Books
    paginate_by = 4
    template_name = 'books/booklist.html'
    context_object_name = 'books'


class BookDetail(generic.DetailView):
    template_name = 'books/detalview.html'
    model = Books


class BookDelete(generic.DeleteView):
    model = Books
    template_name = 'books/delete.html'
    success_url = reverse_lazy('book_list')


class NewBook(generic.CreateView):
    model = Books
    template_name = 'books/newbook.html'
    fields = ['title', 'description', 'price', 'author', 'language', 'cover']


class EditBook(generic.UpdateView):
    model = Books
    template_name = 'books/edit.html'
    fields = ['title', 'description', 'price', 'author', 'language', 'cover']



