from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = 'The Gh Blogs'
admin.site.site_title = 'The Gh Blogs'
admin.site.index_title = 'Gh Blogs | Administration'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("blog.urls")),
]


urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT
    )
urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )