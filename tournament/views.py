from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import TournamentForm
from .models import Tournament


def home(request):
    return render(request, 'tournament/home.html')

def register_page(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = UserCreationForm()
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('login')

        context = {'form':form}
        return render(request, 'tournament/register.html', context)


def login_page(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username,password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username or password is incorrect')

        context = {}
        return render(request, 'tournament/login.html', context)

def logout_page(request):
    logout(request)
    return redirect('login')

def create_tournament(request):
    if request.method == 'GET':
        form = TournamentForm(request.user)
        context = {'form':form}
        return render(request, 'tournament/create.html', context)
    if request.method == 'POST':
        form = TournamentForm(request.user, request.POST or None, request.FILES or None)
        if form.is_valid():
            name = form.cleaned_data['name']
            closeDate = form.cleaned_data['closeDate']
            size = form.cleaned_data['size']
            saving = form.save(commit=False)
            user = request.user
            print(user)
            saving.createdBy = user
            saving.save()
            messages.success(request, 'New tournament created')
            return redirect('home')


def list_all_tournaments(request):
    tournaments = Tournament.objects
    context = {"objects": tournaments}

    return render(request, 'tournament/tournamentlist.html', context)


def list_user_tournaments(request):
    if request.user.is_authenticated:
        tournaments = Tournament.objects.filter(createdBy=request.user.id)
        context = {"objects": tournaments}

        return render(request, 'tournament/usertournamentlist.html', context)
    else:
        return redirect('home')