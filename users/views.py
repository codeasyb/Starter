from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required  # login required decorator
from django.contrib import messages
from .forms import UserRegistrationForm, UserUpdateForm, ProfileUpdateForm

# Create your views here.
def register(request):
	if request.method == 'POST':
		form = UserRegistrationForm(request.POST) # user creation instantiate form POST
		# validating the user 
		if form.is_valid():
			form.save() # saving the form and hash the password
			username = form.cleaned_data.get('username')
			messages.success(request, f'Your account has beed created. You can now login {username.upper()}')
			return redirect('login') # redirect the user to home-page after sign-up
	else:
		form = UserRegistrationForm() # this will instantiate empty form
	return render(request, 'users/register.html', {'form': form})

# adds functionaly to user view of being logged in to see profile view
@login_required
def profile(request):
	if request.method == 'POST':
		user_form = UserUpdateForm(request.POST, instance=request.user) # instances for username, email fields
		profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile) # instances for image field
		# if info is valid then update 
		if user_form.is_valid() and profile_form.is_valid():
			user_form.save()
			profile_form.save()
			messages.success(request, f'Your account has beed updated.')
			return redirect('profile') # send user back to profile page
	else:
		user_form = UserUpdateForm(instance=request.user) 
		profile_form = ProfileUpdateForm(instance=request.user.profile) 

	context = {
		'user_form': user_form,
		'profile_form': profile_form
	}
	return render(request, 'users/profile.html', context)




# option to use
# message.debub
# message.info
# message.success
# message.warning
# message.error