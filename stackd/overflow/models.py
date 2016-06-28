from __future__ import unicode_literals

from django.db import models
import datetime


# Create your models here.

class Question (models.Model):
	author = models.CharField (max_length = 200, default = "anonymous@pandora.com")
	question_title = models.TextField(max_length = 200)
	question_detail = models.TextField(max_length = 200000, default = "no detail")
	tags = models.CharField(max_length = 200)
	pub_date = models.DateTimeField('date published')
	status = models.CharField(max_length = 20)
	upvotes = models.PositiveIntegerField (default = 0)
	downvotes = models.PositiveIntegerField(default = 0)
	def netvotes(self):
		return self.upvotes-self.downvotes
	def __str__(self):
		return self.question_title


class Comment (models.Model):
	question = models.ForeignKey(Question, on_delete = models.CASCADE)
	comment_text = models.TextField(max_length = 200000)
	author = models.CharField (max_length = 200, default = "anonymous@pandora.com")
	upvotes = models.IntegerField(default = 0)
	downvotes = models.IntegerField(default = 0)
	pub_date = models.DateTimeField('date published')
	def __str__(self):
		return self.comment_text
	def netvotes(self):
		return self.upvotes-self.downvotes


class Answer (models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	answer_text = models.TextField(max_length=200000)
	author = models.CharField(max_length=200, default="anonymous@pandora.com")
	upvotes = models.IntegerField(default=0)
	downvotes = models.IntegerField(default=0)
	pub_date = models.DateTimeField('date published')

	def __str__(self):
		return self.comment_text

	def netvotes(self):
		return self.upvotes - self.downvotes