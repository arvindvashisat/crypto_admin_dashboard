from django.shortcuts import render, redirect, get_list_or_404
from django.contrib import messages, auth
from django.contrib.auth.models import User
from .models import CustomUser

def register(request):
  if request.method == 'POST':
    # Get form values
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    password2 = request.POST['password2']
    is_active = request.POST['status']

    # Check if passwords match
    if password == password2:
      # Check username
      if User.objects.filter(username=username).exists():
        return redirect('register')
      else:
        if User.objects.filter(email=email).exists():
          return redirect('register')
        else:
          # Looks good
          user = User.objects.create_user(username=username, password=password,email=email, first_name=first_name, last_name=last_name, is_active=is_active)
          user.save()
          return redirect('login')
    else:
      return redirect('register')
  else:
    return render(request, 'accounts/register.html')

# Login View Function
def login(request):
  if request.session.get('member_id', False):
    return redirect('dashboard')
  else:
    if request.method == 'POST':
      username = request.POST['username']
      password = request.POST['password']

      user = auth.authenticate(username=username, password=password)

      if user is not None:
        auth.login(request, user)
        request.session['member_id'] = user.id
        return redirect('dashboard')
      else:
        messages.error(request, 'Invalid credentials')
        return redirect('login')
    else:
      return render(request, 'accounts/login.html')

# Logout View Function
def logout(request):
  if request.method == 'POST':
    auth.logout(request)
    try:
      del request.session['member_id']
    except KeyError:
      pass
    messages.success(request, 'You are now logged out')
    return redirect('login')

# Dashboard View Function
def dashboard(request):
  if request.session.get('member_id', False):
    return render(request, 'accounts/dashboard.html')

# Profile View Function
def profile(request,user_id):
  users = User.objects.get(pk=user_id)
  profile_users = CustomUser.objects.get(pk=user_id)
  context = {
    'users': users,
    'profile_users':profile_users
  }
  return render(request, 'accounts/profile.html', context)

# Profile View Function
def profile1(request):
  # users = User.objects.get(pk=user_id)
  # profile_users = CustomUser.objects.get(pk=user_id)
  # context = {
  #   'users': users,
  #   'profile_users':profile_users
  #}
  return render(request, 'accounts/profile1.html')

# Profile View Function
def createclient(request):
  return render(request, 'accounts/createclient.html')

def update(request,user_id):
  User.objects.get(pk=user_id)
  first_name = request.POST['first_name']
  last_name = request.POST['last_name']
  email = request.POST['email']
  User.objects.all().update(first_name=first_name,last_name=last_name,email=email)
  return render(request, 'dashboard')



