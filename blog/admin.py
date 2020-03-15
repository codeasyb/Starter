from django.contrib import admin
from .models import Post

# Register your models here.
class PostAdmin(admin.ModelAdmin):
	list_display = ('title', 'status', 'created_on')
	search_fileds = ['title', 'content']
	prepopulated_fields = {'author': ('title',)}

admin.site.register(Post)