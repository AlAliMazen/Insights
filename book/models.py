from django.db import models
from django.contrib.auth.models import User
from django import forms
from cloudinary.models import CloudinaryField
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.


class Author(models.Model):
    """
    gives information about the author of the book
    many authors can have many books, but many books
    can only have one single author
    Shakespear wrote the Merchant of Venice, Romeo & Juliet and....
    George Orwel wrote Animal Farm, 1984 ...

    """
    fullname = models.CharField(max_length=200, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="add_authors")  # noqa
    author_image = CloudinaryField('image', default='placeholder')
    place_of_birth = models.CharField(max_length=200)
    date_of_birth = models.DateField()
    short_biography = models.TextField()
    created_on = models.DateTimeField(auto_now=True)
    approved = models.BooleanField(default=False)

    # metaclass for default view on the admin page
    class Meta:
        ordering = ['-created_on', 'fullname']

    def __str__(self):
        return self.fullname


class Category(models.Model):
    """
    category will be used to specify the book genre whether it is politics,
    economics, sociology, thriller,
    """
    category_name = models.CharField(max_length=200, unique=True)
    category_description = models.TextField()

    class Meta:
        ordering = ['category_name']

    def __str__(self):
        return self.category_name


class Book(models.Model):
    """
    main class for showing books
    """
    title = models.CharField(max_length=200, unique=True)
    writer = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='book_author')  # noqa
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')  # noqa
    slug = models.SlugField(max_length=200, unique=True)
    cover_img = CloudinaryField('image', default='placeholder')
    short_description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    book_category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, related_name="Genre")  # noqa
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on', 'title']

    def __str__(self):
        return self.title


class Review(models.Model):
    """
    for adding reviews on the selected book
    """
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="reviews")  # noqa
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="commenter")  # noqa
    insight = models.TextField(blank=False)
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return self.insight


class Likes(models.Model):
    """
    see how many likes a book has got
    """
    likes = models.BooleanField(default=False)
    liked_book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='liked_book')  # noqa
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="liker")  # noqa
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return str(self.id)


class Rating(models.Model):
    """
    see how many point out of 10 has a book got
    """
    rating = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(10.0)])  # noqa
    rated_book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="rated_book")  # noqa
    user_rated = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_rated')  # noqa
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return str(self.rating)
