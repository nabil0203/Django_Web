
from django.shortcuts import render, redirect
from . import forms                                                             # for all the forms
from django.contrib.auth import authenticate, login, logout                     # for authenticate login and logout
from django.contrib import messages                                             # for the messages

from django.contrib.auth.forms import AuthenticationForm                        # for the login_view

from django.contrib.auth.forms import PasswordChangeForm                        # for the pass_change

from django.contrib.auth import update_session_auth_hash                        # for the pass_change method 1,2
from django.contrib.auth.decorators import login_required                       # for the pass_change method 1,2

from django.contrib.auth.forms import SetPasswordForm                              # for the pass_change method 2



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
            username = form.cleaned_data.get('username')                                    # cleaned_data = errorless data
            password = form.cleaned_data.get('password')                                    # cleaned_data = errorless data
            user = authenticate(username = username, password = password)                           # checks if the user is valid

            if user is not None:                                                          # asholei kono user ke paici kina, paile login+success message
                login(request, user)
                messages.success(request, 'Logged in Successfully')
                return redirect('list_students')
            
            else:
                messages.error(request, 'Invalid Credentials!!!')


    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form' : form})







# -------------------Logout user-------------------

def logout_view(request):
    logout(request)
    messages.success(request, 'Logged Out Successfully')
    return redirect('list_students')







# -------------------Password Change-------------------


# Method-1 : Need old password
# import required
# check settings.py

@login_required                                                     # decorator imported; login required so that none can change the password without logging in
def pass_change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data = request.POST)                   # user = user who already has an account;     data = who is requesting data

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)                          # 'hash' keeps the user logged in after changing the password
            messages.success(request, 'Password Changed Successfully!!!')

            return redirect('list_students')


    else:
        form = PasswordChangeForm(user = request.user)

    return render(request, 'pass_change.html', {'form' : form}) 






# Method-2 : No Old password needed
# same to same as the method-1
# just imported 'SetPasswordForm'
# changed 'PasswordChangeForm' into 'SetPasswordForm'


@login_required
def pass_change2(request):
    if request.method == 'POST':
        form = SetPasswordForm(user=request.user, data = request.POST)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Password Changed Successfully!!!')

            return redirect('list_students')


    else:
        form = SetPasswordForm(user = request.user)

    return render(request, 'pass_change.html', {'form' : form}) 
