from django.urls import path
from django.contrib.auth import views
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('profile', views.profile, name='profile'),
    path('<int:user_id>', views.profile, name='profile'),
    path('update', views.update, name='update'),
    path('<int:user_id>', views.update, name='update'),
    path('profile1', views.profile1, name='profile1'),
    path('createclient', views.createclient, name='createclient'),
]