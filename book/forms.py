from django import forms

from django.forms import ModelForm

from .models import Book, Author, Category,Review

# create a form for a book 

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title','writer','cover_img','short_description','book_category')

class AuthorForm(forms.ModelForm):
    class Meta:
        model=Author
        fields = ('fullname','date_of_birth','author_image','place_of_birth','short_biography')
        # widget=forms.DateInput(format='%d/%m/%Y'),input_formats=['%d/%m/%Y'],
        labels = {
			'fullname': 'Author fullname',
			'date_of_birth': 'Date of Birth',
			'author_image': 'Author Image',
			'place_of_birth': 'Country of origin',
			'short_biography': 'Short biography',			
		}

        widgets = {
			'date_of_birth': forms.DateInput(attrs={'type': 'text', 'placeholder': 'yyyy-mm-dd'}),
		}

class CategoryForm(forms.ModelForm):
    class Meta:
        model=Category
        fields=('category_name','category_description')


class ReviewForm(forms.ModelForm):
    class Meta:
        model=Review
        fields=('insight',)