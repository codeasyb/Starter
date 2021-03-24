from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post

# Create your views here.
def home(request):
	context = {
		'posts': Post.objects.all() # data coming from the server
	}
	# handling how the user will go to our blog home page
	return render(request, 'blog/home.html', context) # rendering the home page using the template

# what model to view
class PostListView(ListView):
	model = Post
	template_name = 'blog/home.html' # <app> / <model> _ <viewtype>.html
	context_object_name = 'posts'
	#ordering = ['-date_posted'] # change list order
	paginate_by = 5


class UserPostListView(ListView):
	model = Post
	template_name = 'blog/user_posts.html' # <app> / <model> _ <viewtype>.html
	context_object_name = 'posts'
	ordering = ['-date_posted'] # change list order
	paginate_by = 5

	def get_queryset(self):
		# if the user exit, will be capturd in the username variable, else return 404
		user = get_object_or_404(User, username=self.kwargs.get('username'))
		return Post.objects.filter(author=user).order_by('-date_posted') # ordering is passed here now

# what model to view
class PostDetailView(DetailView):
	model = Post
	
# what model to view
class PostCreateView(LoginRequiredMixin, CreateView):
	model = Post
	fields = ['title', 'content']

	#if not provided, will [ throw integrity error ]
	# validating the form for the current user logged in
	def form_valid(self, form):
		# form trying to sumbit, take the instance and set the author
		# to the current logged in user
		form.instance.author = self.request.user 
		return super().form_valid(form)

# what model to view
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Post
	fields = ['title', 'content']

	#if not provided, will [ throw integrity error ]
	# validating the form for the current user logged in
	def form_valid(self, form):
		# form trying to sumbit, take the instance and set the author
		# to the current logged in user
		form.instance.author = self.request.user 
		return super().form_valid(form)

	# This is validation for users to not update other users posts
	def test_func(self):
		# get the exact post that is updating
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False

# what model to view
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Post
	success_url = '/'

	# This is validation for users to not update other users posts
	def test_func(self):
		# get the exact post that is updating
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False

def about(request):
	return render(request, 'blog/about.html', {'title': 'About'}) # rendering the about page using the template






