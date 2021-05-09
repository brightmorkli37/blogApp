from django.contrib import admin
from .models import Blog

class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'title', 'date_published')
    list_filter = ('status', 'category')
    search_fields = ('title', 'body')

admin.site.register(Blog, BlogAdmin)
