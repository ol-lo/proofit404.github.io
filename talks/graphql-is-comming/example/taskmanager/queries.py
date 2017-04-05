import graphene
from graphene_django import DjangoObjectType

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

    employees = graphene.List(Employee)
    tasks = graphene.List(Task)

    def resolve_employees(self, args, context, info):

        return EmployeeModel.objects.all()

    def resolve_tasks(self, args, context, info):

        return TaskModel.objects.all()
