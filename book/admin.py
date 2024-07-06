from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Author

# Register your models here.
@admin.register(Author)
class AuthorAdmin(SummernoteModelAdmin):
    list_display=('fullname','place_of_birth','date_of_birth','approved')
    search_fields =['fullname']
    list_filter = ('approved','short_biography')
    summernote_fields=('content',)