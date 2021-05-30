from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='user_logout'),
    path('register/', views.user_signup, name='user_signup'),
    path('<int:id>/', views.detail_view, name='detail_view' ),
    path('category/<str:cats>/', views.category, name='category'),
    path('base/', views.base_template, name='base_template'),
    path('write_post', views.add_blog, name='add_blog'),
]
