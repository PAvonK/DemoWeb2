from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView,
    UpdateView, 
    DeleteView
   )
    #ths allows for the use of class view type ListView, DetialView, CreateView
from .models import Post

# this is the logic for how we want to handle when a user wants to go to our home page
def home(request): #this is a function based view
    # dictionary key / value to connect to posts from above
    context = {
        'posts': Post.objects.all() # pulls from database because of from .models import Post above
    }
    # render is how we return that template 
    return render(request, 'blog/home.html', context)


# here is an example of a class based view, this has much more functionaliy and will handle more of the logic when used. there are different types of views to use in class based views.
class PostListView(ListView): 
    model = Post #technically these are all that is needed to create the list View
    template_name = 'blog/home.html' #<app>/<model>_<viewtype>.html - here are are redirecting the template to this naming convention rather than creating a new template.  We could also here just rename the home template to follow the naming convention listed.
    context_object_name = 'posts' #this is tells home page to loop though the 'posts' since that is what they are called in the home page.
    ordering = ['-date_posted'] #re-orders the posts on the home page from most recent to show first. essentially last to first. if the it was ['date_posted'] without any - it would post them first to last in relation to when they were posted. i.e oldest first
 
class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView): 
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form): 
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin,UpdateView): 
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form): 
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

def about(request):
    # render is how we return that template 
    return render(request, 'blog/about.html', {'title': 'About'})




