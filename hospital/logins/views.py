from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from django.contrib.auth import logout
from .forms import AppointmentForm
from .models import Patient

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

def index(request):
    return render(request, 'logins/index.html')

def logout_view(request):
    logout(request)
    return redirect('index')

def book_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST, user=request.user)
        if form.is_valid():
            appointment = form.save(commit=False)

            if request.user.is_authenticated:
                patient = Patient.objects.get(user=request.user)
                appointment.patient = patient
            else:
                appointment.patient_name = form.cleaned_data.get('patient_name')
                appointment.patient_email = form.cleaned_data.get('patient_email')
                appointment.patient_phone = form.cleaned_data.get('patient_phone')
            appointment.save()
            messages.success(request, f'Your appointment has been created Successfully!')
            return redirect('home') 
    else:
        form = AppointmentForm(user=request.user)

    return render(request, 'logins/appointment.html', {'form': form})
