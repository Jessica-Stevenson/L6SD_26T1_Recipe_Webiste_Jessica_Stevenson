from django.urls import path
from . import views

urlpatterns = [
    #Home
    path('', views.home_view, name='home'),

    #User
    path('signup/', views.signup_view, name='signup'),
    path('profile/', views.profile_view, name='profile'),

    #Recipe management
    path('recipe/create/', views.create_recipe_view, name='create_recipe'),
    path('recipe/delete/<int:pk>/', views.delete_recipe_view, name='delete_recipe'),
    path('recipe/<int:pk>/', views.recipe_detail_view, name='recipe_detail'),

    #Daily Recipes
    path('daily/', views.daily_view, name='daily_all'),

    #Holidays
    path('holidays/', views.holidays_view, name='holidays'),

    #Diet & Health
    path('health_diet/', views.health_diet_view, name='health_diet'),
]