import graphene
from graphene_django import DjangoObjectType

from .models import Choice as ChoiceModel
from .models import Question as QuestionModel


class Question(DjangoObjectType):

    class Meta:

        model = QuestionModel


class Choice(DjangoObjectType):

    class Meta:

        model = ChoiceModel


class Query(graphene.ObjectType):

    questions = graphene.List(Question)

    def resolve_questions(self, args, context, info):

        return QuestionModel.objects.all()


schema = graphene.Schema(query=Query)
