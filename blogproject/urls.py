from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
# from django.views.decorators.csrf import csrf_exempt
# from graphene_django.views import GraphQLView

admin.site.site_header = 'The Gh Blogs'
admin.site.site_title = 'The Gh Blogs'
admin.site.index_title = 'Gh Blogs | Administration'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("blog.urls")),
    path('apiv2/', include("apiv2.urls")),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
