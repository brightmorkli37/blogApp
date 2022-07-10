from rest_framework import serializers
from blog.models import Blog, Category, Comment
from django.contrib.auth import get_user_model



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class BlogSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    comments = serializers.SerializerMethodField()
    
    class Meta:
        model = Blog
        fields = '__all__'

    def get_comments(self, obj):
        return CommentSerializer(obj.comments.all(), many=True).data


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    
    class Meta:
        model = Comment
        fields = ('author', 'post', 'body')


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})

    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'password', 'email', 'first_name', 'last_name')
    
    def create(self, validated_data):
        user = super(UserSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
