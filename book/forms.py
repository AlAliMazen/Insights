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
        # widget=forms.DateInput(format='%d/%m/%Y'),input_formats=['%d/%m/%Y'],
        labels = {
			'name': 'Author fullname',
			'date_of_birth': 'dd/mm/yyyy',
			'author_image': 'Manager',
			'place_of_birth': 'Country of origin',
			'short_biography': 'Short biography',			
		}

        widgets = {
			'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Event Name'}),
			'date_of_birth': forms.DateInput(attrs={'type': 'text', 'placeholder': 'dd.mm.yyyy'}),
		}

class CategoryForm(forms.ModelForm):
    class Meta:
        model=Category
        fields=('category_name','category_description')

