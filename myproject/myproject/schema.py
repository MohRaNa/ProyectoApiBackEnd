import graphene
from graphene_django import DjangoObjectType
from myapp.models import CustomUser

class CustomUserType(DjangoObjectType):
    class Meta:
        model = CustomUser
        field = {"id", "username", "password", "email"}
   
class Query(graphene.ObjectType):
    user = graphene.List(CustomUserType)

    def resolve_user(self, info):
        return CustomUser.objects.all()

schema = graphene.Schema(query=Query)
