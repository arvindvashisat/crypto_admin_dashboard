from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import User, Setting

# Index view
def index(request):
    return render(request, 'dashboard/index.html')

def search(request):
    users = User.objects.all()
    # Find User on first name
    if 'first_name' in request.GET:
        first_name = request.GET['first_name']
        if first_name:
            users = users.filter(username=first_name)

    # Find Users by email id
    if 'email' in request.GET:
        email = request.GET['email']
        if email:
            users = users.filter(email=email)

    # Find Users by status
    if 'status' in request.GET:
        status = request.GET['status']
        if status:
            users = users.filter(is_active=status)

    context = {
        'users': users
    }
    return render(request, 'dashboard/manager.html', context)

def manager(request):
    users = User.objects.all()

    context ={
        'users' : users
    }
    return render(request, 'dashboard/manager.html', context)

def setting(request):
    #settings = Setting.objects.all()
    settings = Setting.objects.get(pk=1)

    context = {
        'settings': settings
    }
    return render(request, 'dashboard/setting.html', context)

def update_setting(request):
    obj = Setting.objects.get(pk=1)
    obj.name = "some_new_value"
    obj.save()

def live_crypto_prices(request):
    return render(request, 'dashboard/live_crypto_prices.html')

