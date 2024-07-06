from . import views
from django.urls import path


# urls for linking and redirecting 

urlpatterns=[
    path('',views.my_author,name='home'),
    path('category/',views.add_category,name='category')
]