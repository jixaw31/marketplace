from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib import messages
from item.models import Category, Item
from .forms import SignUpForm, ItemForm, SearchForm


# Create your views here.


def signUp(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'signed up successfully')
            return redirect('base:index')
    form = SignUpForm()
    return render(request, 'sign_up.html', {'form': form})


def log_in(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'LOGGED IN')
            return redirect('base:index')
        else:
            messages.error(request, 'ERRORED!!')
    return render(request, 'log_in.html')


def log_out(request):
    logout(request)
    messages.success(request, 'logged out')
    return redirect('base:index')


def index(request):
    items = Item.objects.all()
    categories = Category.objects.all()
    page = 'home'
    query = request.GET.get('query')
    if query:
        items = Item.objects.filter(Q(name__icontains=query) | Q(category__name__icontains=query))
    context = {'items': items,
               'categories': categories,
               'query': query,
               'page': page}
    return render(request, 'index.html', context)


# def showCategories(request, pk):
#     # if request.GET.get('query'):
#     #     categories = Category.objects.filter(id=pk)
#     categories = Category.objects.all
#     return render(request, 'index.html', {'categories': categories})


@login_required(login_url='base:log-in')
def addItem(request):
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()
            messages.success(request, 'Item added')
            return redirect('base:index')
    else:
        form = ItemForm()
    return render(request, 'add_item.html', {'form': form})


@login_required(login_url='base:log-in')
def dashboard(request):
    return render(request, 'dashboard.html', {})
