from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from .forms import UserUpdateForm
from .forms import ProfileUpdateForm
from .models import *
from theater.models import theater_list

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in.')
            return redirect ('login')
    else: 

             
        form = UserRegisterForm()
    return render(request,'users/register.html',{'form':form})


    
@login_required
def payment(request):
    if request.method == 'POST':
        banking_name = request.POST['Banking_name']
        account_no = request.POST['Account']
        password = request.POST['password']

        payment = Payment(banking_name=banking_name, account_no=account_no, password=password)
        payment.save()

        obj = Ticket.objects.get(id=18)
        user = User.objects.get(id=1)
        theater = theater_list.objects.get(id=1)
        context = {
            'theater' : theater.theater_name,
            'name': user.username,
            'movie_name':obj.movie_name,
            'date':obj.date,
            'time':obj.time,
            'hall_type':obj.hall_type,
            'total_seat':obj.total_seat
        }  

        return render(request, 'users/printticket.html', context)
    else:
        return render(request, 'users/payment.html',{'title':'Payment'})
    
    
@login_required
def ticketbooking(request):
    if request.method == 'POST':      
        movie_name = request.POST['Movie_name']
        date = request.POST['Date']
        time = request.POST['Time']
        hall_type = request.POST['Hall_type']
        total_seat = request.POST['Total_seat']
        
        tickets = Ticket(movie_name = movie_name, date = date, time = time, hall_type = hall_type, total_seat = total_seat)
        tickets.save()

        return render(request, 'users/payment.html',{'title':'Payment'})
    else:
        return render(request, 'users/ticketbooking.html',{'title':'Book Ticket'})

    
    
@login_required
def printticket(request):  
    
    return render(request, 'users/printticket.html')



@login_required
def profile(request):
    if request.method == 'POST':  
        u_form = UserUpdateForm(request.POST,instance=request.user)
        p_form = ProfileUpdateForm(request.POST, 
                                   request.FILES, 
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f' Your account has been Updater! ')
            return redirect ('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
        
    context = {
        'u_form' : u_form,
        'p_form' : p_form
    }
    
    return render(request, 'users/profile.html', context)























