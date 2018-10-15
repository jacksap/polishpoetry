from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import LoginForm, CommentForm
from django.contrib.auth import authenticate, login, logout
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Poet, Poem, Comment
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Class-Based Views

@method_decorator(login_required, name='dispatch')
class PoetCreate(CreateView):
    model = Poet
    fields = '__all__'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect('/poets/')

@method_decorator(login_required, name='dispatch')
class PoetUpdate(UpdateView):
    model = Poet
    fields = '__all__'
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        return HttpResponseRedirect('/poets/' + str(self.object.pk))

@method_decorator(login_required, name='dispatch')
class PoetDelete(DeleteView):
  model = Poet
  success_url = '/poets'

@method_decorator(login_required, name='dispatch')
class PoemCreate(CreateView):
    model = Poem
    fields = '__all__'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect('/poems/')

@method_decorator(login_required, name='dispatch')
class PoemUpdate(UpdateView):
  model = Poem
  fields = '__all__'
  def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        return HttpResponseRedirect('/poems/' + str(self.object.pk))

@method_decorator(login_required, name='dispatch')
class PoemDelete(DeleteView):
  model = Poem
  success_url = '/poems'

@method_decorator(login_required, name='dispatch')
class CommentUpdate(UpdateView):
    model = Comment
    fields = ['content']

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        return redirect(f"/poems/{self.object.poem_id}")

@method_decorator(login_required, name='dispatch')
class CommentDelete(DeleteView):
   model = Comment
   def post(self, request, *args, **kwargs):
       comment = self.get_object()
       poem_id = comment.poem_id
       comment.delete()
       return redirect(f"/poems/{poem_id}")

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
    comment_form = CommentForm()
    return render(request, 'poems/detail.html', {
    	'poem': poem, 'comment_form': comment_form
    })

@method_decorator(login_required, name='dispatch')
def add_comment(request, poem_id):
    form = CommentForm(request.POST)
    if form.is_valid():
        new_comment = form.save(commit=False)
        new_comment.poem_id = poem_id
        new_comment.save()
    return redirect('poems_detail', poem_id=poem_id)