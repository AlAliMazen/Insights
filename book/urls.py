from . import views
from django.urls import path


# urls for linking and redirecting 

urlpatterns=[
    path('',views.BooksList.as_view(),name='home'),
    path('add_book/', views.add_book, name='add-book'),
    path('add_author/', views.add_author, name='add-author'),
    path('add_category/', views.add_category, name='add-category'),
]