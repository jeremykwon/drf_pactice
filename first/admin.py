from django.contrib import admin
from .models import Post, ContentPost


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('pk', 'text')
    search_fields = ('text', 'pk')  # admin 에 검색 기능 추가


@admin.register(ContentPost)
class PostAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'content')
