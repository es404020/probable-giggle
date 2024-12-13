from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseNotFound,Http404,HttpResponseRedirect
from . import models
from django.urls import reverse,reverse_lazy
from .forms import CarForm
from django.contrib import messages
from django.views.generic import TemplateView,FormView,CreateView,ListView,DetailView,UpdateView,DeleteView
from my_app.models import Car
articles ={
    'sport':'sport page',
    'finance':'finance page',
   'politics':'politics page',
}



def simple_view(request):
    my_var = {'first_name':'Eniola','last_name':'Ajani','some_list':[1,2,4] ,'status':True}
    return render(request,'my_app/example.html',context=my_var) #

def variable(request):
     return render(request,'my_app/variable.html') #
def list_user(request):
    all_users = models.Patient.objects.all()
    users = {'uses':all_users}
    print(all_users);
    print("all_users");
    return render(request,'my_app/list.html',context=users) #
 


def list(request):
    all_cars = models.Car.objects.all()
    cars = {'cars':all_cars}
    return render(request,'my_app/list.html',context=cars) #


def add(request):
    if request.POST:
        # brand = request.POST['brand']
        # year = int(request.POST['year'])
        form = CarForm(request.POST)
        if form.is_valid():
            
            form.save()
            messages.success(request, 'created ')
            return redirect(reverse('my_app:list'))
    else:
        form = CarForm()
  
        return render(request,'my_app/add.html',context={"forms":form}) #

def delete(request):
    if request.POST:
        pk = request.POST['pk']
        models.Car.objects.get(pk=pk).delete()
        return redirect(reverse('my_app:list'))
    else:
        return render(request,'my_app/delete.html') #
    




class HomeView(TemplateView):
    
    template_name = 'my_app/example.html'


class AddFormView(FormView):
     form_class= CarForm
     template_name = 'my_app/add.html'

     success_url = reverse_lazy("my_app:list")

     def form_valid(self, form):
         
       if form.is_valid():
            
            print(form.cleaned_data)
         
            return super().form_valid(form)
     
     def get(self, request, **kwargs):
        context = self.get_context_data()
        print(context['view'])
        
        # Add additional logic, maybe htmx or something else.
        
        return render(request, self.template_name, context={"forms":context['form']})
     


class CarView(CreateView):
    model = Car
    fields = "__all__"
    success_url = reverse_lazy("my_app:list")

class ListView(ListView):
    model = Car
    queryset = Car.objects.order_by('year')

class DetailView(DetailView):
    model = Car


class CarUpdate(UpdateView):
    model = Car
    fields = ['brand','year']
    success_url = reverse_lazy("my_app:list")

class CarDelete(DeleteView):
    model = Car

    success_url = reverse_lazy("my_app:c_list")




