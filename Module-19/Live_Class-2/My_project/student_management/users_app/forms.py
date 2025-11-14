
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import User


class UserRegisterForm(UserCreationForm):

    class Meta:
        model = User

#       fields = '__all__'                                 # all the inbuilt features of register is not required, only needed are mentioned below

        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']                             # password2 = confirm password



