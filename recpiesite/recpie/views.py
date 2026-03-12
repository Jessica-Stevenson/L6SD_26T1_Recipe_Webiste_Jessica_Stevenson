from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from .models import Recipe
from .models import Profile

@login_required
def profile_view(request):
    profile = Profile.objects.get(user=request.user)
    return render(request, 'registration/profile.html', {'profile': profile})

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

def recpie_detail_view(request, pk):
    recpie = get_object_or_404(Recipe, pk=pk)
    return render(request, 'food/recpie_detail.html', {'recpie': recpie})