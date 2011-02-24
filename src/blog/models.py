from django.db import models
from django.contrib import admin 
from django.contrib.auth.models import User

class BlogPost(models.Model):
  title = models.CharField(max_length=150)
  body = models.TextField()
  timestamp = models.DateTimeField()
  class Meta: 
    ordering = ('-timestamp',)
	
class BlogPostAdmin(admin.ModelAdmin):
  list_display = ('title', 'timestamp')

class PostNews(models.Model):
  title = models.CharField(max_length=150)
  short_text =  models.TextField()
  body = models.TextField()
  timestamp = models.DateTimeField()
  class Meta: 
    ordering = ('-timestamp',)

class NewsAdmin(admin.ModelAdmin):
  list_display = ('id', 'short_text', 'title', 'timestamp')
  
# Register BlogPost in model admin
admin.site.register(BlogPost, BlogPostAdmin) 
admin.site.register(PostNews, NewsAdmin) 
