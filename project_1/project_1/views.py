from django.http import HttpResponse

def homepage(request):
    return HttpResponse("this is homepage")
def contact(request):
    return HttpResponse("this is my contact page")