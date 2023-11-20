from django.shortcuts import render, redirect, get_object_or_404
from core.models import User
from listings.models import Listing
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from listings.models import Listing
from inquiry.models import inquiry
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth.hashers import check_password
from listings.forms import UpdateForm

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['password']
        password2 = request.POST['password2']
        user = User

        context ={
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
            'username': username,
            'phone': phone,
            'password': password,
        }

        if password == password2:
            if user.objects.filter(username=username).exists():                                                                                              
                messages.error(request, 'Username is already taken')
                return redirect('register')
            else:
                if user.objects.filter(email=email).exists():
                    messages.error(request, 'Email is already in use')
                    return redirect('register')
                else:
                    if user.objects.filter(phone=phone).exists():
                        messages.error(request, 'Contact no. is already in use')
                        return redirect('register')
                    elif len(phone)!=10:
                        messages.error(request, 'Contact no. is not valid')
                    
                        return redirect('register')
                    else:
                        user = user.objects.create_user(username=username, email=email, password=password,  phone=phone, first_name=first_name, last_name=last_name)
                        user.save()
                        login(request, user)
                        messages.success(request, 'You  are now logged in!')
                        return redirect('home')

                       
        else:
            messages.error(request,'Passwords do not match')
            return redirect('register')                
        
    else:
        return render(request, 'acounts/register.html')  

def userlogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You are now logged in!')
            return redirect('home')
        else:
            messages.error(request, 'Invalid Credentials!')
            return redirect('login')
    else:
        return render(request, 'acounts/login.html')

@login_required
def userlogout(request):
    if request.method == 'POST':
        logout(request)
        messages.success(request, "You are now logged out!")
        return redirect('home')        

@login_required
def dashboard(request):
    mylistings = Listing.objects.order_by('-list_date').filter(owner=request.user)
    context = {
        'listings': mylistings
    }
    return render(request, 'acounts/dashboard.html', context)        

@login_required
def favourite_listing(request):
    favourites = request.user.favourites
    favourites = favourites.split(',')[1:]
    print(favourites)
    listings = []
    for i in favourites:
        listings.append(get_object_or_404(Listing,pk=int(i)))
    context = {
        'listings': listings
    }
    return render(request, 'acounts/favourites.html', context)
@login_required
def myinquiries(request):
    myinquiry = inquiry.objects.all().filter(user_id=request.user.id)
    context = {
        'myinquiries': myinquiry
    }
    return render(request, 'acounts/dashboard_myinquiries.html', context)

@login_required
def inquiry1(request):
    myinquiry = inquiry.objects.all().filter(owner_id=request.user.id)
    context = {
        'inquiries': myinquiry
    }
    return render(request, 'acounts/dashboard_inquiries.html', context)

@login_required
def send_reply(request):
    if request.method =="POST":
        email = request.POST['email']
        message = request.POST['message']
        lisiting = request.POST['listing']
        send_mail(
            'Reply from ' + lisiting + ' owner',
            message,
            'abhishekdubey6103@gmail.com',
            [email],
            fail_silently=False
        )
        messages.success(request, 'Your reply has been sent successfully')
        return redirect('inquiry1')
    else:
        return redirect('dashboard')    

@login_required
def change_password(request):
    if request.method=='POST':
        user = request.user
        currentpassword = request.POST['currentpassword']
        if not check_password(currentpassword,user.password):
            messages.error(request,'Incorrect Current Password')
            return redirect('dashboard')
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            user.set_password(password1)
            user.save()
            messages.success(request,'You have been logged out')
            messages.success(request,'You have successfully changed the password')
            messages.success(request,'Use your new password to login')
            return redirect('login')
        else:
            messages.error(request,'Passwords do not match')
        return redirect('dashboard')
    
    else:
        return render(request,'acounts/change_password.html')

