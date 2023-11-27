# myproject/urls.py
from django.urls import path
from graphene_django.views import GraphQLView
from  myapp.schema import schema

urlpatterns = [
    # Otras rutas de tu aplicación Django
    path('graphql/', GraphQLView.as_view(graphiql=True, schema=schema)),
]
