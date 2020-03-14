from django.db import models
from django.contrib.auth.models import User
from PIL import Image


# Create your models here.
# when making changes to the model you make changes in the database

class Profile(models.Model):
	# when user deletes its account then everything gets deleted of that user
	# casacde meands that if the user is deleted then the profile is deleted 
	user = models.OneToOneField(User, on_delete=models.CASCADE) 
	# directory when images get uploaded to when user uploads the images
	image = models.ImageField(default='default.jpg', upload_to='profile_pics')

	# when ever the profile prints then prints the name of the user
	def __str__(self):
		return f"{self.user.username} Profile"


	def save(self, *args, **kwargs):
		super(Profile, self).save(*args, **kwargs)

		img = Image.open(self.image.path)
		if img.height > 300 or img.width > 300:
			output_size = (300, 300)
			img.thumbnail(output_size)
			img.save(self.image.path)