from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('muscleinfo', views.muscleinfo, name='muscleinfo'),
    path('getplans', views.getplans, name='getplans'),
    path('login', views.handleLogin, name='handelLogin'),
    path('logout', views.handleLogout, name='handleLogout'),
    path('signup', views.handleSignup, name='handleSignup'),
    path('counter', views.counter, name='counter'),
    path("Signup", views.Signup, name="Signup"),
    path("test", views.test, name="test"),
    path("nutrition", views.nutrition, name="nutrition"),
    path("plans", views.plans, name="plans"),
    path("diet", views.diet, name="diet"),



]
