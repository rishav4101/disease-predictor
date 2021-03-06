from django.urls import path
from . import views

app_name = 'authentication'

urlpatterns = [
    path('register/<str:role>/', views.registerView, name='register'),
    path('login/', views.loginView, name='login'),
    path('logout/', views.logoutView, name='logout'),
]