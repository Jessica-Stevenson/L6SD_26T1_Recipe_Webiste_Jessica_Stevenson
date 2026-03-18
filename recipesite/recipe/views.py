from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .models import Recipe, Profile
from .forms import RecipeForm

#Recipe
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
def delete_recipe_view(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    if recipe.user != request.user:
        return HttpResponseForbidden("You cannot delete this recipe.")
    if request.method == "POST":
        recipe.delete()
        return redirect('home')
    return render(request, 'food/delete_recipe.html', {'recipe': recipe})


def recipe_detail_view(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    return render(request, 'food/recipe_detail.html', {'recipe': recipe})

@login_required
def edit_recipe_view(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)

    if recipe.user != request.user:
        return HttpResponseForbidden("You cannot edit this recipe.")

    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('recipe_detail', pk=recipe.pk)
    else:
        form = RecipeForm(instance=recipe)

    return render(request, 'food/edit_recipe.html', {'form': form, 'recipe': recipe})

#User
@login_required
def profile_view(request):
    profile = Profile.objects.get(user=request.user)
    return render(request, 'registration/profile.html', {'profile': profile})


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


#Home
def home_view(request):
    q = request.GET.get('q')
    if q:
        recipes = Recipe.objects.filter(title__icontains=q).order_by('-created_at')
    else:
        recipes = Recipe.objects.all().order_by('-created_at')
    return render(request, 'home.html', {'recipes': recipes})


#Daily Recipes
def daily_view(request):
    subcat = request.GET.get('subcategory')
    recipes = Recipe.objects.filter(
        main_category='daily',
        sub_category=subcat
    ).order_by('-created_at') if subcat else Recipe.objects.filter(main_category='daily').order_by('-created_at')

    template_name = f'food/daily/{subcat}.html' if subcat else 'food/daily/all.html'
    return render(request, template_name, {'recipes': recipes})


#Holidays
def holidays_view(request):
    subcat = request.GET.get('subcategory')
    recipes = Recipe.objects.filter(
        main_category='holiday',
        sub_category=subcat
    ).order_by('-created_at') if subcat else Recipe.objects.filter(main_category='holiday').order_by('-created_at')

    template_name = f'food/holidays/{subcat}.html' if subcat else 'food/holidays/all.html'
    return render(request, template_name, {'recipes': recipes})


#Diet & Health
def health_diet_view(request):
    subcat = request.GET.get('subcategory')
    recipes = Recipe.objects.filter(
        main_category='health',
        sub_category=subcat
    ).order_by('-created_at') if subcat else Recipe.objects.filter(main_category='health').order_by('-created_at')

    template_name = f'food/health/{subcat}.html' if subcat else 'food/health/all.html'
    return render(request, template_name, {'recipes': recipes})