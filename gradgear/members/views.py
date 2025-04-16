from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def welcome(request):
    template = loader.get_template('welcome.html')
    return HttpResponse(template.render())
def signup(request):
    template = loader.get_template('signup.html')
    return HttpResponse(template.render())
def signin(request):
    template = loader.get_template('login.html')
    return HttpResponse(template.render())
# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import SignUpForm, SignInForm
from django.contrib import messages

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request, "Account created successfully. Please sign in.")
            return redirect('signin')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def signin(request):
    if request.method == 'POST':
        form = SignInForm(request, data=request.POST)
        if form.is_valid():
            user = authenticate(
                request, 
                username=form.cleaned_data['username'], 
                password=form.cleaned_data['password']
            )
            if user is not None:
                login(request, user)
                return redirect('members')  # or your home page
            else:
                messages.error(request, "Invalid username or password.")
    else:
        form = SignInForm()
    return render(request, 'signin.html', {'form': form})

def signout(request):
    logout(request)
    return redirect('signin')