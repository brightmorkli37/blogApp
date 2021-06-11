import graphene
from graphene import relay
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from blog.models import Blog


class Blogs(DjangoObjectType):
    class Meta:
        model = Blog
        filter_fields = ('author', 'title')
        interfaces = (relay.Node, )
        # fields = "__all__"

class Query(graphene.ObjectType):
    blogsifo = relay.Node.Field(Blogs)
    all_blogs = DjangoFilterConnectionField(Blogs)

    def resolve_blogsinfo(self, info):
        return Blog.objects.all()

schema = graphene.Schema(query=Query)