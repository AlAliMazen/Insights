from django.shortcuts import render, get_object_or_404,reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from .models import Author,Book,Category,Review
# Create your views here.



class BooksList(generic.ListView):
    queryset = Book.objects.all()
    template_name="book/index.html"
    paginated_by=3



def book_list(request):
    queryset = Book.objects.all()
    book = get_object_or_404(queryset)
    print("about to render the the page")
    return render(request,
                  'book/index.html',
                  {
                      "book": book
                  })


def my_author(request):
    """
    Display authors  :model: book.Author
    """
    return HttpResponse("<h1>Hello my author</h1>")


def add_category(request):
    """
    Display Category  :model: book.Category
    """
    return HttpResponse("<h1>Category</h1>")


def add_book(request):
    """
    Display Book  :model: book.book
    """
    return HttpResponse("<h1>Add Books</h1>")

def add_comment(request):
    """
    Display Book  :model: book.book
    """
    return HttpResponse("<h1>Comment</h1>")