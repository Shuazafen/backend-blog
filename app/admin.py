from django.contrib import admin
from .models import *

# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content', 'image', 'create_at']
    search_fields = ['title', 'content']
    readonly_fields = ['create_at']
    list_filter = ['create_at']
    # list_display = ['blog', 'user', 'created_at', 'comment']


class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'blog', 'content', 'created_at']
    search_fields = ['id', 'content']
    readonly_fields = ['created_at']
    list_filter = ['created_at']

class LikeAdmin(admin.ModelAdmin):
    list_display = ['id', 'blog', 'like', 'created_at']
    search_fields = ['id', 'blog', 'like']
    readonly_fields = ['created_at']
    list_filter = ['created_at']  

class NewsletterAdmin(admin.ModelAdmin):
    list_display = ['id', 'email', 'created_at']
    search_fields = ['email']
    readonly_fields = ['created_at']
    list_filter = ['created_at']   

admin.site.register(Blog, BlogAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Like, LikeAdmin)
admin.site.register(Newsletter, NewsletterAdmin)