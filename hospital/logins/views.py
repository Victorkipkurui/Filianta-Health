from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from django.contrib.auth import logout


def sign_up(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your account has been created Successfully!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'logins/signup.html', {'form': form})


@login_required
def home(request):
    return render(request, 'logins/home.html')

def base(request):
    return render(request, 'logins/base.html')

def logout_view(request):
    logout(request)
    return redirect('base')

@login_required
def profile(request):
    return render(request, 'logins/profile.html')