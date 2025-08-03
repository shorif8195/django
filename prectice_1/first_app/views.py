from django.shortcuts import render
from . import django_form
# Create your views here.
def home(request):
    if(request.method  == 'POST'):
        name = request.POST.get('name')
        email = request.POST.get('email')
        print(name,email)
        return render(request,'home.html',{'name':name,'email':email})
    
    return render(request,'login.html')

def login(request):

    return render(request,'login.html')

def django_form_func(request):
    form = django_form.Django_form()

    return render(request,'django_form.html',{'form':form})
    

    
    