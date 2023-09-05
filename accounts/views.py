from django.shortcuts import render, redirect
from .forms import UserRegistrationFrom
from django.contrib.auth import authenticate, login, logout


def home(request):
    return render(request, 'index.html')

def user_login(request):
    if request.method == 'POST':
        user_name = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=user_name, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'accounts/login.html', {'Error': 'Invalid Username or Password'})
    return render(request, 'accounts/login.html')


def subscribe(request):
    form = UserRegistrationFrom()
    Error = ''
    if request.method == 'POST':
        form = UserRegistrationFrom(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            Error = 'Fill the form correctly'
    return render(request, 'accounts/subscribe.html', {'Error': Error})


def logout_user(request):
    logout(request)
    return redirect('home')


def contact(request):
    return render(request, 'contact.html')