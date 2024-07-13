from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Author, Category, Book, Review, Likes, Rating

# Register your models here.
@admin.register(Author)
class AuthorAdmin(SummernoteModelAdmin):
    list_display=('fullname','place_of_birth','date_of_birth','approved')
    search_fields =['fullname']
    list_filter = ('approved','short_biography')
    summernote_fields=('short_biography',)


@admin.register(Category)
class CategoryAdmin(SummernoteModelAdmin):
    list_display=("id","category_name")
    search_fields=['category_name']
    summernote_fields=('category_description',)


@admin.register(Book)
class BookAdmin(SummernoteModelAdmin):
    list_display = ('id','title','writer','book_category')
    search_fields = ['title','writer']
    list_filter = ('title','created_on',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('short_description',)

@admin.register(Review)
class ReviewAdmin(SummernoteModelAdmin):
    list_display=('book','author','insight','approved')
    search_fields=['book','author']
    list_filter=('book','author',)
    summernote_fields=('insight',)


@admin.register(Likes)
class LikesAdmin(admin.ModelAdmin):
    list_display = ('id', 'liked_book','user_id','created_on')
    search_fields=['liked_book']
    list_filter=('liked_book',)


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('id','rated_book','rating', 'user_rated','created_on')
    search_fields=['rated_book']
    list_filter=('rated_book',)