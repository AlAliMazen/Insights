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