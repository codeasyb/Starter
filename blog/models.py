from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField()
	date_posted = models.DateTimeField(default=timezone.now) # we do not want to exectue the now by [ now() ]
	author = models.ForeignKey (User, on_delete=models.CASCADE) # if the user is deleted then the post will be deleted

	def __str__(self):
		return self.title

	# get any instance of post
	def get_absolute_url(self):
		# return will return full path as a string, and for posts that users will create
		# needs a specific pk using [ kwards ]
		return reverse('post-detail', kwargs={'pk': self.pk})