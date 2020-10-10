from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import contacts
from .models import *


def home(request):
    return render(request, 'theater/home.html')

def about(request):
    return render(request, 'theater/about.html', {'title':'About'})

@login_required
def nowshowing(request):
    return render(request, 'theater/nowshowing.html', {'title':'Now Showing'})

def ticketprice(request):
    return render(request, 'theater/ticketprice.html', {'title':'ticket Price'})

def aynabaji(request):
    return render(request, 'theater/aynabji.html', {'title':'Aynabaji'})

def contact(request):
    if request.method == 'POST':
        uname = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        subject= request.POST['subject']

        contact=contacts(name=uname, email=email,message=message,subject=subject)
        contact.save()

        return render(request, 'theater/contact.html',{'title':'Contact'})
    else:
        return render(request, 'theater/contact.html',{'title':'Contact'})
    

            
        
        
        
