from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegistrationForm(UserCreationForm):
	email = forms.EmailField()

	# this keeps the configuration in one place
	class Meta:
		# model that is going to get effected is the user model
		model = User 
		# this is the template for the user to create a form
		fields = ['username', 'email', 'password1', 'password2'] 


# user update form, will allows us to update username and email
class UserUpdateForm(forms.ModelForm):
	email = forms.EmailField()

	class Meta:
		model = User 
		fields = ['username', 'email'] 

# profile update form, will allow us to update image
class ProfileUpdateForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['image']