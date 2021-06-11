from django.conf import settings
from graphene_django import DjangoObjectType

from .models import Blog
import graphene

class BlogType(DjangoObjectType):
    class Meta:
        model = Blog

class Query(graphene.ObjectType):
    all_posts = graphene.List(BlogType)

    def resolve_all_posts(root, info):
        return (
            Blog.objects.all()
        )

schema = graphene.Schema(query=Query)