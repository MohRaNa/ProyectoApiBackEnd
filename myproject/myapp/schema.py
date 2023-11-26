import graphene
from graphene_django.types import DjangoObjectType
from .models import CustomUser

class UserType(DjangoObjectType):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email']

class Query(graphene.ObjectType):
    user = graphene.Field(UserType, id=graphene.Int())
    all_users = graphene.List(UserType)

    def resolve_user(self, info, id):
        return CustomUser.objects.get(pk=id)

    def resolve_all_users(self, info):
        return CustomUser.objects.all()

schema = graphene.Schema(query=Query)
