from django.shortcuts import render
from .models import Post
from django.http import HttpResponse

# this is the logic for how we want to handle when a user wants to go to our home page
def home(request):
    # dictionary key / value to connect to posts from above
    context = {
        'posts': Post.objects.all() # pulls from database because of from .models import Post above
    }
    # render is how we return that template 
    return render(request, 'blog/home.html', context)

def about(request):
    # render is how we return that template 
    return render(request, 'blog/about.html', {'title': 'About'})



