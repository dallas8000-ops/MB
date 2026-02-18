from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'message', 'created_at')
    search_fields = ('author', 'message')
    ordering = ('-created_at',)
