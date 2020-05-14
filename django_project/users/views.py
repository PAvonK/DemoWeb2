from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm

# create a form for user input
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST) #existing form in the .forms file that we created there
        if form.is_valid(): # this valididy check makes sure things like, is this a new user? do they already exist?, do that passwords match etc...
            form.save() #Creats the users in the database, does the password hashing and everything else
            username = form.cleaned_data.get('username')
            messages.success(request, f'You account has been created, You are now able to log in') #flash message which displays if we have recieved correct data (it only displays once)
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required # this decorator is used prior to the function in order to make sure that the person must be logged in to view the profile page
def profile(request):
    return render(request, 'users/profile.html')
