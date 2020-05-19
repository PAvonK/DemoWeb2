from django.urls import path
from .views import (
    PostListView, 
    PostDetailView, 
    PostCreateView,
    PostUpdateView,
    PostDeleteView
)
from . import views

urlpatterns = [
    # The mapping for the path in the views function in views.py (blog home in this case)
    # Since this is the home of the blog page it only needs an empty string
    # path('', views.home, name='blog-home'), # this vies.home is the implimentation of the function based view in blog.views
    # The mapping for the path in the views function in views.py (blog about in this case)
    path('', PostListView.as_view(), name='blog-home'),  # this is the implimentation of the class based biew
    # unlinke home, about needs the about/ ro map it
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='blog-about'),
]

# PostListView is looking for a template at with <app>/<model>_<viewtype>.html as convention