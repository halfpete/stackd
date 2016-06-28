from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Question, Comment
from django.utils import timezone
from django.template import loader, RequestContext
from django.db import connection

def index(request):
	question_list = Question.objects.order_by('-pub_date')
	template = loader.get_template('overflow/index.html')
	context = {
	'question_list': question_list,
	}
	return HttpResponse(template.render(context, request))

def detail(request, question_id):
	question = Question.objects.get(id = question_id)
	comment_list = question.comment_set.all().order_by('-upvotes')
	context = {
	'question': question,
	'comment_list': comment_list,
	}
	return render(request, 'overflow/detail.html', context)

def add_new_question_to_database(request, title, detail, tags, email):
	q = Question(question_title = title, question_detail = detail, tags = tags, author = email, pub_date = timezone.now(), status = 'unsolved')
	q.save()

def add_comment_to_question(request, question, text, email):
	c = Comment(question = question, comment_text = text, author = email, pub_date = timezone.now())
	c.save()