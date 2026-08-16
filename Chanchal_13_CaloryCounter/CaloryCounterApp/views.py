from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from CaloryCounterApp.forms import *

# Create your views here.

def home_view(request):

    return render(request, 'home.html')


def register_view(request):

    form_data = registerForm()

    if request.method == 'POST':
        form_data = registerForm(request.POST)
        if form_data.is_valid():
            user_data = form_data.save()

            login(request, user_data)

            return redirect('profile_view')
            
    context = {
        'form': form_data,
        'title': 'Register Account',
        'btn': 'Register'
    }

    return render(request, 'base_form.html', context)


def login_view(request):

    form_data = AuthenticationForm()

    if request.method == 'POST':
        form_data = AuthenticationForm(request, data = request.POST)
        if form_data.is_valid():
            user_data = form_data.get_user()
            login(request, user_data)
            return redirect('dashboard_view')
            
    context = {
        'form': form_data,
        'title': 'Login Account',
        'btn': 'Login'
    }

    return render(request, 'base_form.html', context)


def logout_view(request): 

    logout(request)

    return redirect('login_view')


@login_required
def profile_view(request):

    try:
        user_data = profileModel.objects.get(user=request.user)
    except:
        user_data = profileModel.objects.create(user=request.user)

    context = {
        'user_data' : user_data,
    }

    return render(request, 'profile_view.html', context)


@login_required
def update_profile(request):

    try:
        user_data = profileModel.objects.get(user=request.user)
    except:
        user_data = profileModel.objects.create(user=request.user)


    form_data = profileUpdateForm(instance=user_data)
    
    if request.method == 'POST':
        form_data = profileUpdateForm(request.POST, instance=user_data)
        if form_data.is_valid():
            data = form_data.save(commit=False)

            age = int(data.age)
            height = float(data.height)
            weight = float(data.weight)

            if data.gender == 'Male':
                data.bmr = round(66.47 + (13.75*weight) + (5.003*height) - (6.755*age), 2)
            elif data.gender == 'Female':
                data.bmr = round(655.1 + (9.563*weight) + (1.85*height) - (4.676*age), 2)
            else:
                data.bmr = 0
            data.save()

            return redirect('profile_view')

    context = {
        'form' : form_data,
        'title':"Profile update",
        'btn':"update",
    }
    return render(request, 'base_form.html', context)




    

    
