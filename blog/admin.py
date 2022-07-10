from django.contrib import admin
from .models import Blog, Category, Comment


class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'body', 'date_added')
    search_fields = ('author', 'body')
   

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date_published')
    list_filter = ('status', 'category')
    search_fields = ('title', 'body')


admin.site.register(Blog, BlogAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Category)
