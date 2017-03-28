from django.db import models


class Question(models.Model):

    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    class Meta:

        verbose_name = 'question'
        verbose_name_plural = 'questions'


class Choice(models.Model):

    question = models.ForeignKey(Question, related_name='choices')
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    class Meta:

        verbose_name = 'choice'
        verbose_name_plural = 'choices'
