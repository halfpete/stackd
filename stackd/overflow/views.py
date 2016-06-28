from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Question, Comment
from django.utils import timezone

def index(request):
    return render (request, 'overflow/index.html')

def add_new_question_to_database(request, title, detail, tags, email):
	q = Question(question_title = title, question_detail = detail, tags = tags, author = email, pub_date = timezone.now(), status = 'unsolved')
	q.save()

def add_comment_to_question(request, question, text, email):
	c = Comment(question = question, comment_text = text, author = email, pub_date = timezone.now())
	c.save()