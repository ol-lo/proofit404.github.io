from django.conf.urls import url
from graphene_django.views import GraphQLView

from .schema import schema

urlpatterns = [
    url(
        r'^$',
        GraphQLView.as_view(schema=schema, graphiql=True),
        name='graphql',
    ),
]
