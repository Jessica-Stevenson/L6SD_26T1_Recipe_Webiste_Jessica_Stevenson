from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('health_diet/', views.health_diet_view, name='health_diet'),
    path('holidays/', views.holidays_view, name='holidays'),
    path('signup/', views.signup_view, name='signup'),
    path('breakfast/', views.breakfast_view, name='breakfast'),
    path('lunch/', views.lunch_view, name='lunch'),
    path('dinner/', views.dinner_view, name='dinner'),
    path('recipe/<int:pk>/', views.recpie_detail_view, name='recpie_detail'),
    path('profile/', views.profile_view, name='profile'),
]