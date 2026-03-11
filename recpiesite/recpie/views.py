from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

def home_view(request):
    return render(request, 'home.html')

def health_diet_view(request):
    return render(request, 'food/health_diet.html')

def holidays_view(request):
    return render(request, 'food/holidays.html')

def breakfast_view(request):
    return render(request, 'food/daily/breakfast.html')

def lunch_view(request):
    return render(request, 'food/daily/lunch.html')

def dinner_view(request):
    return render(request, 'food/daily/dinner.html')

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()

    return render(request, 'registration/signup.html', {'form': form})