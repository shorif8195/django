from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def courses(request):
    return HttpResponse("This is courses page.")

def home(request):
    return HttpResponse("This is first app page.")
