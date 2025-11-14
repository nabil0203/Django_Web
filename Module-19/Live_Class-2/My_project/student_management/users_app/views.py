
from django.shortcuts import render, redirect
from . import forms
from django.contrib.auth import authenticate, login
from django.contrib import messages

from django.contrib.auth.forms import AuthenticationForm



# Create your views here.


# -------------------Register new user-------------------

def register_view(request):
    
    if request.method == 'POST':
        form = forms.UserRegisterForm(request.POST)    

        if form.is_valid():
            user = form.save()                                         # after saving the form, an user will be created
            login(request, user)                                       # user create er sathe sathei login hobe
            messages.success(request, 'Account Created Successfully')
            return redirect('list_students')


    else:
        form = forms.UserRegisterForm()

    return render(request, 'register.html', {'form' : form})






# -------------------Login new user-------------------

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)    

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username = username, password = password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Logged in Successfully')
                return redirect('list_students')
            
            else:
                messages.error(request, 'Invalid Credentials!!!')


    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form' : form})
