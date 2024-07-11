from django.shortcuts import render, get_object_or_404,reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from .models import Author,Book,Category,Review
from .forms import BookForm, AuthorForm, CategoryForm



# Create your views here.

class BooksList(generic.ListView):
    queryset = Book.objects.all()
    template_name="book/index.html"
    paginate_by=6

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

def transform_string(input_string): 
    # Convert all characters to lowercase
    lowercase_string = input_string.lower()
    # Replace spaces with hyphens
    transformed_string = lowercase_string.replace(' ', '-')
    return transformed_string


def add_book(request):
    """
    Display Book  :model: book.book
    """
    submitted = False
    if request.method == "POST":
        print("POST function")
        bookForm = BookForm(request.POST, request.FILES)
        if bookForm.is_valid():
            print("Book form is valid")
            book = bookForm.save(commit=False)
            print(f'{request.user}  | {book.title}')
            book.user = request.user
            book.slug = transform_string(book.title)
            print(f"Book slug: {book.slug}")
            book.save()
            submitted = True
            bookForm = BookForm()  # Reset the form after successful submission
            messages.add_message(
                request, messages.SUCCESS,
                f'{book.title} has been added successfully'
            )
            return HttpResponseRedirect('/add_book?submitted=True')
        else:
            print("Book form is not valid", bookForm.errors)
    else:
        bookForm = BookForm()
        if 'submitted' in request.GET:
            submitted = True

    return render(request, "book/add_book.html", {'bookForm': bookForm, 'submitted': submitted})


def add_author(request):
    """
    Adding author to the database
    """
    submitted = False
    if request.method == 'POST':
        authorForm = AuthorForm(request.POST, request.FILES)
        if authorForm.is_valid():
            author = authorForm.save(commit=False)
            author.user = request.user
            author.save()
            submitted = True
            authorForm = AuthorForm()  # Reset form after submission
            messages.add_message(
                request, messages.SUCCESS,
                f'{author.fullname} has been added successfully'
            )
            return HttpResponseRedirect('/add_author?submitted=True')
        else:
            print("Author form is not valid:", authorForm.errors)  # Debugging statement
    else:
        authorForm = AuthorForm()
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'book/add_author.html', {'authorForm': authorForm, 'submitted': submitted})



def add_category(request):
    """
    Display Category  :model: book.Category
    """
    submitted = False
    if request.method == 'POST':
        categoryForm = CategoryForm(request.POST)
        if categoryForm.is_valid():
            categoryForm.save()
            submitted = True
            categoryForm = CategoryForm()
            return HttpResponseRedirect('/add_category?submitted=True')
        else:
            print("Category Form has an error", categoryForm.errors)
    else:
        categoryForm=CategoryForm()
        if 'submitted' in request.GET:
            submitted = True

    return render(request,'book/add_category.html', {'categoryForm':categoryForm, 'submitted': submitted})
    


def add_comment(request):
    """
    Display Book  :model: book.book
    """
    return HttpResponse("<h1>Comment</h1>")