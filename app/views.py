from django.shortcuts import render, redirect
from .forms import UserRegisterForm, UserLoginForm
from django.contrib.auth import authenticate, login, logout

def index_view(request):

    return render(request, 'app/index.html')

def index_rolls(request):

    return render(request, 'app/rolls.html')

def index_set(request):

    return render(request, 'app/set.html')

def index_napitki(request):

    return render(request, 'app/napitki.html')

def user_register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('index')
    form = UserRegisterForm()

    return render(request, 'app/user_register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user:
                login(request, user)
                return redirect('index')

    form = UserLoginForm()

    return render(request, 'app/user_login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('index')



