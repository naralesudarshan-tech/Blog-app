from django.contrib import admin
from .models import Post, Category, Comment

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date_posted', 'category')
    list_filter = ('date_posted', 'category')
    search_fields = ('title', 'content')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'post', 'date_posted')
    list_filter = ('date_posted',)

admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Comment, CommentAdmin)