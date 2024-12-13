
from django import forms
from django.forms import ModelForm
from .models import Car


class CarForm(forms.Form):
    brand = forms.CharField(label='Brand Name')
    year = forms.IntegerField(label='Year')


# class CarForm(ModelForm):
#     class Meta:
#         model = Car
#         fields = "__all__"