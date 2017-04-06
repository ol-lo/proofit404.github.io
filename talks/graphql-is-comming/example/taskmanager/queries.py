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
        filter_fields = {
            'title': ['exact', 'icontains', 'startswith'],
            'description': ['exact'],
        }
        interfaces = (relay.Node,)


class TaskQuery(AbstractType):

    task = relay.Node.Field(Task)
    all_tasks = DjangoFilterConnectionField(Task)


class Query(TaskQuery, graphene.ObjectType):

    employees = graphene.List(Employee)
    tasks = graphene.List(Task)
    debug = graphene.Field(DjangoDebug, name='__debug')

    def resolve_employees(self, args, context, info):

        return EmployeeModel.objects.all()

    def resolve_tasks(self, args, context, info):

        return TaskModel.objects.all()
