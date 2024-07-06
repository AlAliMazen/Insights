from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Author, Category, Book

# Register your models here.
@admin.register(Author)
class AuthorAdmin(SummernoteModelAdmin):
    list_display=('fullname','place_of_birth','date_of_birth','approved')
    search_fields =['fullname']
    list_filter = ('approved','short_biography')
    summernote_fields=('content',)


@admin.register(Category)
class CategoryAdmin(SummernoteModelAdmin):
    list_display=("id","category_name")
    search_fields=['category_name']
    summernote_fields=('content',)


@admin.register(Book)
class BookAdmin(SummernoteModelAdmin):
    list_display = ('id','title','writer','book_category')
    search_fields = ['title','writer']
    list_filter = ('title','created_on',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)