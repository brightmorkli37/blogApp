import graphene
from graphene_django import DjangoObjectType
from blog.models import Blog


class BlogsType(DjangoObjectType):
    class Meta:
        model = Blog
        fields = ('author', 'title')
        # fields = "__all__"


class Query(graphene.ObjectType):

    all_blogs = graphene.List(BlogsType)


schema = graphene.Schema(query=Query)