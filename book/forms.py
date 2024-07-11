from django import forms

from django.forms import ModelForm

from .models import Book, Author, Category

# create a form for a book 

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title','writer','cover_img','short_description','book_category')

class AuthorForm(forms.ModelForm):
    class Meta:
        model=Author
        fields = ('fullname','date_of_birth','author_image','place_of_birth','short_biography')
    

class CategoryForm(forms.ModelForm):
    class Meta:
        model=Category
        fields=('category_name','category_description')

