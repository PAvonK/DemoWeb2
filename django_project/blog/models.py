from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User # to import the user from user table

"""
The class is what determines what is going to be in the database.

More specifically, the class determines the table of the database and attribute will be a different field in the database
""" 
class Post(models.Model): #inheriting from models module
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
        # the models.DateTimeField could be set to (auto_now=True) which updates the time for when the post is updated, it can also be (auto_now_add=True) which means it only posts the time of the original post but cannot be changed.  instead we import timezone and do the above so we can change the time if need be manually
    author = models.ForeignKey(User, on_delete=models.CASCADE) # ForeignKey passes in the other table with the argument User as well in this case a command on_delete which states if the user is deleted = models.CASCADE whih means thier posts get deleted also. 

    # defines a return to print out by the title
    def __str__(self):
        return self.title

