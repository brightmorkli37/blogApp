from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = 'Pythoneering Django Admin'
admin.site.site_title = 'Pythoneering Django'
admin.site.index_title = 'Project Administration'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("blog.urls")),
    path('api/', include("app_api.urls")),
    path('authenticate/', include('rest_framework.urls')),
   
]


urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT
    )
urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )