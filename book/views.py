from django.shortcuts import render, get_object_or_404,reverse, redirect
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from .models import Author,Book,Category,Review,Likes,Rating
from .forms import BookForm, AuthorForm, CategoryForm, ReviewForm, LikesForm
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
    
    #ratings
    book_rating_set=Rating.objects.filter(rated_book=book)
    average_rating=book_rating_set.aggregate(Avg('rating'))['rating__avg']
    #reviews to show on a specific book
    reviews=book.reviews.all().order_by("-created_on")

    reviews_count=book.reviews.filter(approved=True).count()

    #handling the post request
    if request.method=='POST':
        userReview=ReviewForm(request.POST)
        if userReview.is_valid():
           print("in the review form again")
           single_review=userReview.save(commit=False)
           single_review.book=book
           single_review.author = request.user
           single_review.save()
           userReview=ReviewForm()
           messages.add_message(request, messages.SUCCESS,'Review submitted and awaiting approval')
           
    
    #likes count
    likes=book.liked_book.count()
    all_likes=book.liked_book.all()
    user_liked_book=False
    for user_like in all_likes:
        if user_like.user_id == request.user:
            user_liked_book = True
    

    # form for submitting a like
    likes_form=LikesForm
    userReview=ReviewForm()
    print("About to render the books insights")
    return render(request, "book/book_insight.html",
                  {
                    'book':book,
                    'author_details':author_details ,
                    'likes':likes,
                    'ratings':average_rating,
                    'reviews':reviews,
                    'reviews_count':reviews_count,
                    'userReview':userReview,
                    'likes_form':likes_form,
                    'all_likes':all_likes,
                    'user_liked_book':user_liked_book
                    },)


def edit_review(request, slug, review_id):

    """
    edit the selected review
    """
    print(f"in the edit form {slug}  |  {review_id}",)
    if request.method == "POST":
        queryset = Book.objects.filter(approved=True)
        book=get_object_or_404(queryset,slug=slug)
        review=get_object_or_404(Review, pk=review_id)
        review_form=ReviewForm(data=request.POST,instance=review)

        if review_form.is_valid() and review.author==request.user:
            insight=review_form.save(commit=False)
            insight.book=book
            insight.approved=False
            insight.save()
            messages.add_message(request, messages.SUCCESS, 'Insight Updated!')

        else:
            messages.add_message(request, messages.ERROR, 'Error updating insight!')
    
    return HttpResponseRedirect(reverse('book_insight',args=[slug]))


def delete_review(request, slug, review_id):
    """
    delete a review from a book
    """
    #queryset = Book.objects.filter(approved=True)
    #book = get_object_or_404(queryset, slug=slug)
    review = get_object_or_404(Review, pk=review_id)

    if review.author == request.user:
        review.delete()
        messages.add_message(request, messages.SUCCESS, "Review deleted!")
    else:
        messages.add_message(request, messages.ERROR, "Only your own review ")
    
    return HttpResponseRedirect(reverse('book_insight',args=[slug]))

