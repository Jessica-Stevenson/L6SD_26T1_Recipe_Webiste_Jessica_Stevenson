from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('about/', views.about_view, name='about'),
    path('recpie/', views.recpie_view, name='recpie'),
    path('signup/', views.signup_view, name='signup'),
]