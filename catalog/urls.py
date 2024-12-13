from django.contrib import admin
from django.urls import path,include
from .views import home_view,ModelCreateView,ModelDetailView,ModelDetailView,ModelDeleteView,CreateUserView
app_name = 'catalog'
urlpatterns =   [
  
    path("", home_view ,name='index'),
    path("book_create", ModelCreateView.as_view() ,name='book_create'),
    path("book_detail/<int:pk>", ModelDetailView.as_view() ,name='book_detail'),
    path("book_delete/<int:pk>", ModelDeleteView.as_view() ,name='book_delete'),
     path("signup/", CreateUserView.as_view(),name="signup"),
 
]
