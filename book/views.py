from django.shortcuts import render, get_object_or_404,reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from .models import Author,Book,Category,Review,Likes,Rating
from .forms import BookForm, AuthorForm, CategoryForm, ReviewForm
from django.db.models import Avg


# Create your views here.

class BooksList(generic.ListView):
    queryset = Book.objects.filter(approved=True)
    template_name="book/index.html"
    paginate_by=6

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


def book_insight(request,slug):
    #book
    queryset = Book.objects.all()
    book=get_object_or_404(queryset, slug=slug)
    # author
    book_author = book.writer
    author_details=get_object_or_404(Author, fullname=book_author)
    #likes
    likes=book.liked_book.count()
    #ratings
    book_rating_set=Rating.objects.filter(rated_book=book)
    average_rating=book_rating_set.aggregate(Avg('rating'))['rating__avg']
    #reviews
    reviews=Review.objects.filter(book=book.id)

    # Review form
    userReview=ReviewForm()
    #handling the post request

    if request.method=='POST':
        userReview=ReviewForm(request.POST)
        if userReview.is_valid():
           print("in the inner if")
           single_review=userReview.save(commit=False)
           single_review.book=book
           single_review.author = request.user
           single_review.save()
           messages.add_message(
                request, messages.SUCCESS,
                'Review submitted and awaiting approval'
            )
           userReview=ReviewForm()
    print("About to render the books insights")
    return render(request, "book/book_insight.html",
                  {
                    'book':book,
                    'author_details':author_details ,
                    'likes':likes,
                    'ratings':average_rating,
                    'reviews':reviews,
                    'userReview':userReview
                    })


def add_review(request, id):
    """
    Display Book  :model: book.book
    """
    submitted = False
    print("in the function")
    if request.method =='POST':
        print("Any thing")
        reviewForm=ReviewForm(request.POST)
        book = get_object_or_404(Book,book_id=id)
        print(f'{book.title}')
        if reviewForm.is_valid():
           reviewForm.save(commit=False)
           reviewForm.book=book
           reviewForm.author= request.user
           reviewForm.save()
           messages.add_message(
                request, messages.SUCCESS,
                'Review submitted and awaiting approval'
            )
           submitted =True
        else:
            reviewForm = ReviewForm()

    return render(request,"book/book_insight.html/",{'reviewForm':reviewForm})