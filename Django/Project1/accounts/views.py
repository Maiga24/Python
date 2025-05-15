from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def login_view(request):
    if request.method == 'POST':
        user = authenticate(
            request,
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user:
            login(request, user)
            return redirect('ajouter_facture') 
        messages.error(request, 'Identifiants incorrects')
    return render(request, 'accounts/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if not User.objects.filter(username=username).exists():
            User.objects.create_user(username=username, password=password)
            return redirect('login')
        messages.error(request, 'Nom d’utilisateur déjà utilisé')
    return render(request, 'accounts/register.html')


