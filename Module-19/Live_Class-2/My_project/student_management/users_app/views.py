
from django.shortcuts import render, redirect
from . import forms
from django.contrib.auth import authenticate, login
from django.contrib import messages



# Create your views here.

def register_view(request):
    
    if request.method == 'POST':
        forms = forms.UserRegisterFrom(request.POST)

        if form.is_valid():
            user = form.save()                          # after saving the form, an user will be created
            login(request, user)                        # user create er sathe sathei login hobe
            return redirect('home')


    else:
        form = forms.UserRegisterFrom()

    return render(request, 'register.html', {'form' : form})
