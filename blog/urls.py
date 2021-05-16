from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>/', views.detail_view, name='detail_view' ),
    path('category/<str:cat>/', views.category_view, name='category_view')
]
