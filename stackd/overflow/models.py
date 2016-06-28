from __future__ import unicode_literals

from django.db import models
import datetime


# Create your models here.


class Question(models.Model):
    author = models.EmailField
    question_title = models.TextField(max_length=200)
    question_detail = models.TextField
    tags = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    status = models.CharField(max_length=20)
    upvotes = models.PositiveIntegerField(default=0)
    downvotes = models.PositiveIntegerField(default=0)
    netvotes = models.IntegerField(default=0)

    def __str__(self):
        return self.question_title


class Comment(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    comment_text = models.CharField(max_length=200)
    author = models.EmailField
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)
    netvotes = models.IntegerField(default=0)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.comment_text
