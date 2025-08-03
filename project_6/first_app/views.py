from django.shortcuts import render, redirect

# Create your views here.
from . import models
def home(request):
    student = models.Student.objects.all()

    return render(request, 'home.html',{'data':student})

def delete_student(request,roll):
    std = models.Student.objects.get(pk=roll).delete()
    return redirect('homepage')