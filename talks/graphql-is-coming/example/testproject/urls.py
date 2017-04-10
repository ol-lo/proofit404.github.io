from django.conf.urls import include, url
from django.contrib import admin
from graphene_django.views import GraphQLView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/login/', admin.site.login),
    url(r'^graphql/', GraphQLView.as_view(graphiql=True)),
    url(
        r'^taskmanager/',
        include('taskmanager.urls', namespace='taskmanager'),
    ),
]
