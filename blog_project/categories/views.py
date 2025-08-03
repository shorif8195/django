from django.shortcuts import render, redirect

# Create your views here.
from . import forms

def add_category(request):
    if request.method=='POST':

        category_form = forms.CategoryForm(request.POST)
        if category_form.is_valid():
            category_form.save()
            return redirect('add_category')
        
    else:
        category_form = forms.CategoryForm()

        return render(request,'add_categories.html',{'form': category_form})