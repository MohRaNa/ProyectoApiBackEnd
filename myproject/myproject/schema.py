import graphene
from graphene_django import DjangoObjectType
from myapp.models import CustomUser

class CustomUserType(DjangoObjectType):
    class Meta:
        model = CustomUser
        field = {"id", "username", "password", "email"}

class CreateUserMutation(graphene.Mutation):
    class Arguments:
        username = graphene.String()
        password = graphene.String()
        email = graphene.String()
    
    user = graphene.Field(CustomUserType)
        
    def mutate(self, info, username, password, email):
        user = CustomUser(username=username, password=password, email=email)
        user.save()
        return CreateUserMutation(user=user)


class Query(graphene.ObjectType):
    user = graphene.List(CustomUserType)
    username = graphene.Field(CustomUserType, username=graphene.String())

    def resolve_user(self, info):
        return CustomUser.objects.all()
    def resolve_username(self, info, username):
        return CustomUser.objects.get(username=username)
    
class Mutation(graphene.ObjectType):
    createuser = CreateUserMutation.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
