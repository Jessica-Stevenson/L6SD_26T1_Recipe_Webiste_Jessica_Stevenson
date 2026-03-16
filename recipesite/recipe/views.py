from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from .models import Recipe
from .models import Profile
from .forms import RecipeForm
from django.http import HttpResponseForbidden

@login_required
def delete_recipe_view(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)

    if recipe.user != request.user:
        return HttpResponseForbidden("You cannot delete this recipe.")

    if request.method == "POST":
        recipe.delete()
        return redirect('home')

    return render(request, 'food/delete_recipe.html', {'recipe': recipe})

@login_required
def create_recipe_view(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.user = request.user
            recipe.save()
            return redirect('home') 
    else:
        form = RecipeForm()

    return render(request, 'food/create_recipe.html', {'form': form})

@login_required
def profile_view(request):
    profile = Profile.objects.get(user=request.user)
    return render(request, 'registration/profile.html', {'profile': profile})

def home_view(request):
    recipes = Recipe.objects.all().order_by('-created_at')
    return render(request, 'home.html', {'recipes': recipes})

def breakfast_view(request):
    recipes = Recipe.objects.filter(main_category='daily', sub_category='breakfast').order_by('-created_at')
    return render(request, 'food/daily/breakfast.html', {'recipes': recipes})

def lunch_view(request):
    recipes = Recipe.objects.filter(main_category='daily', sub_category='lunch').order_by('-created_at')
    return render(request, 'food/daily/lunch.html', {'recipes': recipes})

def dinner_view(request):
    recipes = Recipe.objects.filter(main_category='daily', sub_category='dinner').order_by('-created_at')
    return render(request, 'food/daily/dinner.html', {'recipes': recipes})

def holidays_view(request):
    recipes = Recipe.objects.filter(main_category='holiday').order_by('-created_at')
    return render(request, 'food/holidays.html', {'recipes': recipes})

def health_diet_view(request):
    recipes = Recipe.objects.filter(main_category='health').order_by('-created_at')
    return render(request, 'food/health_diet.html', {'recipes': recipes})

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

def recipe_detail_view(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    return render(request, 'food/recipe_detail.html', {'recipe': recipe})
