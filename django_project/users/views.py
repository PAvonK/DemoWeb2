from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm

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
    if request.method == 'POST': #ultimately shis check if the request is POST data, if it is then it changes the data, if it is not then it leaves it the same
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'You account has been updated!') #simple flash message that shows success on updating. 
            return redirect('profile') #re directs them back to the profile page
    else:
        u_form = UserUpdateForm(instance=request.user) # (instance=request.user) makes sure that the data is prefilled in on the forms for user
        p_form = ProfileUpdateForm(instance=request.user.profile) # instance=request.user.profile makes sure that the data is prefilled in on the forms for user profile

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context)
