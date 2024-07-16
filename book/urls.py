from . import views
from django.urls import path


# urls for linking and redirecting 

urlpatterns=[
    path('',views.BooksList.as_view(),name='home'),
    path('add_book/', views.add_book, name='add_book'),
    path('add_author/', views.add_author, name='add_author'),
    path('add_category/', views.add_category, name='add_category'),
    path('<slug:slug>/', views.book_insight, name='book_insight'),
    path('<slug:slug>/edit_review/<int:review_id>', views.edit_review, name='edit_review'),
    path('<slug:slug>/delete_review/<int:review_id>', views.delete_review, name='delete_review'),   
    
]