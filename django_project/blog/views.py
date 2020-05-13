from django.shortcuts import render
from django.http import HttpResponse

# Dummy data / normally this would come from database
posts = [
    {
        'author': 'Phil von Kaenel',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 27, 2018'
    },
    {
        'author': 'Tiesha von Kaenel',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'August 28, 2019'
    }
]

# this is the logic for how we want to handle when a user wants to go to our home page
def home(request):
    # dictionary key / value to connect to posts from above
    context = {
        'posts': posts
    }
    # render is how we return that template 
    return render(request, 'blog/home.html', context)

def about(request):
    # render is how we return that template 
    return render(request, 'blog/about.html', {'title': 'About'})



