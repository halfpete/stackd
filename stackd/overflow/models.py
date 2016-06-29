from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.base_user import AbstractBaseUser

MAX_USERNAME_LENGTH = 60
MAX_AUTHOR_LENGTH = 200
MAX_TITLE_LENGTH = 200
MAX_RESP_LENGTH = 20000
MAX_TAG_LENGTH = 200
MAX_STAT_LENGTH = 20


# Create your models here.

class Question(models.Model):
    author = models.CharField(max_length=MAX_AUTHOR_LENGTH, default="anonymous@pandora.com")
    question_title = models.TextField(max_length=MAX_TITLE_LENGTH)
    question_detail = models.TextField(max_length=MAX_RESP_LENGTH, default="no detail")
    tags = models.CharField(max_length=MAX_TAG_LENGTH)
    pub_date = models.DateTimeField('date published', null=True, default='1950-01-01')
    status = models.CharField(max_length=MAX_STAT_LENGTH)
    upvotes = models.PositiveIntegerField(default=0)
    # userID = models.PositiveIntegerField(default = 0)
    downvotes = models.PositiveIntegerField(default=0)

    def netvotes(self):
        return self.upvotes - self.downvotes

    def __str__(self):
        return self.question_title


class Tag(models.Model):
    name = models.CharField(max_length=50)


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_text = models.TextField(max_length=MAX_RESP_LENGTH)
    author = models.CharField(max_length=MAX_AUTHOR_LENGTH, default="anonymous@pandora.com")
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)
    pub_date = models.DateTimeField('date published', null=True, default='1950-01-01')

    def __str__(self):
        return self.comment_text

    def netvotes(self):
        return self.upvotes - self.downvotes


class AnswerComment(models.Model):
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    comment_text = models.TextField(max_length=MAX_RESP_LENGTH)
    author = models.CharField(max_length=MAX_AUTHOR_LENGTH, default="anonymous@pandora.com")
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)
    pub_date = models.DateTimeField('date published', null=True, default='1950-01-01')

    def __str__(self):
        return self.comment_text

    def netvotes(self):
        return self.upvotes - self.downvotes


class Comment(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    comment_text = models.TextField(max_length=MAX_RESP_LENGTH)
    author = models.CharField(max_length=MAX_AUTHOR_LENGTH, default="anonymous@pandora.com")
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)
    pub_date = models.DateTimeField('date published', null=True, default='1950-01-01')

    def __str__(self):
        return self.comment_text

    def netvotes(self):
        return self.upvotes - self.downvotes


# object.pk for primary key

# class UserManager(BaseManager)


class User(AbstractBaseUser):
    # XXX: Possible to just make this the email?
    username = models.CharField(max_length=MAX_USERNAME_LENGTH, unique=True)

    USERNAME_FIELD = 'username'

    # Keep some unique information about the user
    # XXX: Do we want to require all of this information?
    email = models.CharField(max_length=MAX_USERNAME_LENGTH, unique=True)
    first_name = models.CharField(max_length=MAX_USERNAME_LENGTH)
    last_name = models.CharField(max_length=MAX_USERNAME_LENGTH)

    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']

    def is_active(self):
        # XXX: Always returns true lol
        return True

    def get_full_name(self):
        return "%s %s" % (self.first_name, self.last_name)

    def set_short_name(self):
        return self.first_name
