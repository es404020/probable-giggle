from django.urls import path
# from . import views
from . import views
from .views import AddFormView,CarView,ListView,DetailView,CarUpdate,CarDelete

app_name = 'my_app'

urlpatterns = [

    path('',views.simple_view,name='index'),
    path('variable',views.variable,name='variable'),
    path('list',views.list,name='list'),
    path('add',views.add,name='add'),
    path('delete',views.delete,name='delete'),
    path('cadd',AddFormView.as_view(),name='cadd'),
    path('aadd',CarView.as_view(),name='aadd'),
    path('c_list',ListView.as_view(),name='c_list'),
     path('car_detail/<int:pk>',DetailView.as_view(),name='dd'),
    path('car_update/<int:pk>',CarUpdate.as_view(),name='up'),  
      path('car_delete/<int:pk>',CarDelete.as_view(),name='dd'),  
]