from django.db import models
from django.contrib.auth.models import User
from PIL import Image # this imports Image from the pillow library which allows us to resize the images on save

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) # casscade here set the the on-delete so that if the user is deleted so will all in thier profile.
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self): #this 
        super().save()

        img = Image.open(self.image.path) # We open the image here for resizing

        if img.height > 300 or img.width > 300: # Here is where we use the pillow library in order to save the image at a reduced size... Essentially, if the image is over 300 by 300, then it resizes it down to 300 by 300
            output_size = (300, 300) 
            img.thumbnail(output_size)
            img.save(self.image.path)

