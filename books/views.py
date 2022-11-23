from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, render


from .models import Books
from .forms import CommentForm


class BookList(generic.ListView):
    model = Books
    paginate_by = 4
    template_name = 'books/booklist.html'
    context_object_name = 'books'


# class BookDetail(generic.DetailView):
#     template_name = 'books/detalview.html'
#     model = Books

def detail_view(request, pk):
    book = get_object_or_404(Books, pk=pk)
    book_comment = book.comments.all()
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.book = book
            new_comment.user = request.user
            new_comment.save()
            comment_form = CommentForm()
    else:
        comment_form = CommentForm()

    return render(request, 'books/detalview.html', {
            'books': book,
            'comment': book_comment,
            'comment_form': comment_form,
        })


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



