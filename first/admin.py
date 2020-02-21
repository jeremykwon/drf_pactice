from django.contrib import admin
from .models import Post, ContentPost


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('pk', 'text')


@admin.register(ContentPost)
class PostAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'content')
