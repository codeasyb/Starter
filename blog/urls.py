from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView
from . import views

# end all routes with trailing [ / ] 
# every route needs an template
urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'), 							# send the user to the home route
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'), 	# send the user to the home route
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'), 			# route to show the post with an id
    path('post/new/', PostCreateView.as_view(), name='post-create'), 				# Route to create a new post
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'), 	# route to show the post with an id
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'), 	# route to show the post with an id
    path('about/', views.about, name='blog-about'), 								# send user to the blog route
]



