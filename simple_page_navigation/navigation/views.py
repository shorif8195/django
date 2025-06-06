from django.shortcuts import render
import datetime
# Create your views here.
def about(request):
    d = {'author': 'shorif', 'age':20, 'courses':[
        {
            'id':1,
            'name':'Python',
            'fee' : 500
        },
        {
            'id':2,
            'name': 'Django',
            'Fee': 2000
        },

    ],
    'date': datetime.datetime.now(),
    }
    return render(request,'navigation/about.html',d)

def contact(request):
    return render(request,'navigation/contact.html')