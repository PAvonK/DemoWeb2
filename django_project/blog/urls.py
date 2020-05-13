from django.urls import path
from . import views

urlpatterns = [
    # The mapping for the path in the views function in views.py (blog home in this case)
    # Since this is the home of the blog page it only needs an empty string
    path('', views.home, name='blog-home'),
    # The mapping for the path in the views function in views.py (blog about in this case)
    # unlinke home, about needs the about/ ro map it
    path('about/', views.about, name='blog-about'),
]