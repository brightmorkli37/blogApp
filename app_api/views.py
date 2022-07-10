from django.shortcuts import render
from rest_framework import viewsets, permissions, mixins # , generics
from rest_framework.validators import ValidationError
from blog.models import Blog, Category, Comment
from .serializers import BlogSerializer, CategorySerializer, UserSerializer, CommentSerializer
from django.contrib.auth import get_user_model



class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [permissions.IsAuthenticated]   

    # def get_queryset(self):
    #     return self.queryset.filter(author=self.request.user)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def delete(self, request, *args, **kwargs):
        blog = Blog.objects.filter(id=kwargs['pk'], author=self.request.user)
        if blog.exists():
            return self.destroy(request, *args, **kwargs)
        else:
            raise ValidationError('You are not authorized to delete this blog')


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    # def get_queryset(self):

    #     post = Blog.objects.get(id=self.kwargs['pk'])
    #     return Comment.objects.get(post=post)
    

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # def get_queryset(self):
    #     return self.queryset.filter(username=self.request.user)
