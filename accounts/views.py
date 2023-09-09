from django.shortcuts import render, redirect
from .forms import UserRegistrationFrom
from articles.models import CategoryModel
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
    context = {}
    Error = ''
    form = UserRegistrationFrom()
    if request.method == 'POST':
        form = UserRegistrationFrom(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            Error = 'Fill the form correctly'
    context['form'] = form
    context['Error'] = Error
    return render(request, 'accounts/subscribe.html', context)


def logout_user(request):
    logout(request)
    return redirect('home')


def contact(request):
    context = {}
    all_categories = CategoryModel.objects.all()
    context['all_categories']= all_categories
    return render(request, 'contact.html', context)