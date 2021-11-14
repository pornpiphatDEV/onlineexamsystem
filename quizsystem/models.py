from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    # Delete profile when user is deleted
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.png', upload_to='profile_pics')

    def __str__(self):
        # show how we want it to be displayed
        return f'{self.user.username} Profile'

    def save(self):
        super().save()
        img = Image.open(self.image.path)  # Open image
        # resize image
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)  # Resize image
           
            img.save(self.image.path)
