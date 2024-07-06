from django.shortcuts import render, get_object_or_404,reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from .models import Author
# Create your views here.


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