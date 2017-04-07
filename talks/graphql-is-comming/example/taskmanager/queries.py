import graphene
from graphene import AbstractType, relay
from graphene_django import DjangoObjectType
from graphene_django.debug import DjangoDebug
from graphene_django.filter import DjangoFilterConnectionField

from .models import Comment as CommentModel
from .models import Employee as EmployeeModel
from .models import Status as StatusModel
from .models import Task as TaskModel


class Comment(DjangoObjectType):

    class Meta:

        model = CommentModel


class Employee(DjangoObjectType):

    class Meta:

        model = EmployeeModel
        exclude_fields = ('user', 'password', 'status')


class Status(DjangoObjectType):

    class Meta:

        model = StatusModel


class Task(DjangoObjectType):

    class Meta:

        model = TaskModel


class Query(graphene.ObjectType):

    viewer = graphene.Field(Employee)
    employees = graphene.List(Employee)
    task = graphene.Field(Task, id=graphene.Int())
    tasks = graphene.List(Task, limit=graphene.Int())
    debug = graphene.Field(DjangoDebug, name='__debug')

    def resolve_viewer(self, args, context, info):

        return context.user

    def resolve_employees(self, args, context, info):

        return EmployeeModel.objects.all()

    def resolve_task(self, args, context, info):

        return TaskModel.objects.get(pk=args.get('id'))

    def resolve_tasks(self, args, context, info):

        return TaskModel.objects.all()
