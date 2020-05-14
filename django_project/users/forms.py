from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm): #inherits from the UserCreationForm and allows us to make changes to it.
    email = forms.EmailField() #this is the field to add, the other fields already exist in the base UserCreationForm

    class Meta:
        model = User #specifices which class that we want this form to interact with.
        fields = ['username', 'email', 'password1', 'password2']