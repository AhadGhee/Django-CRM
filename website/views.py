from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.

#Creating homepage view 

def home(request): 
    # Check to see if logging in
    if request.method == 'POST':
        username = request.POST['username'] #assigning what usert typed in to the forms
        password = request.POST['password']
        #Authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged in!")
            return redirect('home')
        else:
            messages.success(request, "There was an Error Logging in...Please try again!")
            return redirect('home')

    else:
        return render(request, 'home.html', {})
    #the request is homepage, we return home.html

def login_user(request):
    pass

def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out..")
    return redirect('home')

def register_user(request):
    return render(request, 'register.html', {})


# Anytime you go to a website, you are requesting that website. That request can sent back 
# into the backend and we pass it in to the view and return something. 