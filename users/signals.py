from django.db.models.signals import post_save # send a single when the object is created
from django.contrib.auth.models import User  # sending the signal to the user
from django.dispatch import receiver # for receiving the signal
from .models import Profile

# we want a user profile to be created for every user
# when the user is created, send this signal. And signal will be saved by {post_save}
@receiver(post_save, sender=User) # when the user is saved send a signal 
def create_profile(sender, instance, created, **kwargs):
	# create an instance when the user is created/ create a profile of the user
	if created:
		Profile.objects.create(user=instance)

# instance is for the user
# save the user profile
@receiver(post_save, sender=User) # when the user is saved send a signal 
def save_profile(sender, instance, **kwargs):
	instance.profile.save()

