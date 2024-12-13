from django.shortcuts import render
from django.http import HttpResponse
from .models import Genre,Language,Author,Book,BookInstance
from django.views.generic import CreateView,DetailView,DeleteView
from django.urls import reverse,reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth.forms import UserCreationForm

@login_required
def home_view(request):
    num_books = Book.objects.all().count()
    books = BookInstance.objects.filter(borrower=request.user)
    num_instance = BookInstance.objects.all().count()
    num_instance_avail =  BookInstance.objects.filter(status__exact='a').count()
    # user = User.objects.get(username=request.user.username)
 
    context ={
        "num_books":num_books,
        "num_instance":num_instance,
        "num_instance_avail":num_instance_avail,
        "books":books
    }


    return  render(request,'catalog/home.html',context=context)


class ModelCreateView(LoginRequiredMixin,CreateView):
    model = Book
    fields ="__all__"
    success_url = reverse_lazy("catalog:index")


class ModelDetailView(LoginRequiredMixin,DetailView):
    model = Book

class ModelDeleteView(LoginRequiredMixin,DeleteView):
    model = Book
    success_url = reverse_lazy("catalog:index")
 
 


class CreateUserView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name ='catalog/signup.html'