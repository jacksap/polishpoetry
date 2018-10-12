from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import LoginForm
from django.contrib.auth import authenticate, login, logout
from .models import Poet, Poem
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def index(request):
  return render(request, 'index.html')

def learn(request):
  return render(request, 'learn.html') 

def login_view(request):
    if request.method == 'POST':
        # if post, then authenticate (user submitted username and password)
        form = LoginForm(request.POST)
        if form.is_valid():
            u = form.cleaned_data['username']
            p = form.cleaned_data['password']
            user = authenticate(username = u, password = p)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/')
                else:
                    print("The account has been disabled.")
                    return HttpResponseRedirect('/')
            else:
                print("The username and/or password is incorrect.")
                return HttpResponseRedirect('/')
    else:
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
        return render(request, 'signup.html', {'form': form})

def poets_index(request):
	poets = Poet.objects.all()
	return render(request, 'poets/index.html', { 'poets': poets })

def poets_detail(request, poet_id):
    poet = Poet.objects.get(id=poet_id)
    return render(request, 'poets/detail.html', {'poet':poet})

def poems_index(request):
	poems = Poem.objects.all()
	return render(request, 'poems/index.html', { 'poems': poems })

def poems_detail(request, poem_id):
    poem = Poem.objects.get(id=poem_id)
    return render(request, 'poems/detail.html', {'poem':poem})