from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
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
    email = request.POST.get('email_field', '')
    new_comment = request.POST.get('comment', '')

    if (email != '' and new_comment != ''):
        add_comment_to_question(request, question, new_comment, email)
    comment_list = question.comment_set.order_by('-pub_date')
    context = {
    'question': question,
    'comment_list': comment_list,
    }

    upvote = request.POST.get('upvote')
    downvote = request.POST.get('downvote')
    if (upvote != None):
        upvote_object(request, )


    return render(request, 'overflow/detail.html', context)

def post(request):
    email = request.POST.get('email_field', '')
    title = request.POST.get('title', '')
    detail = request.POST.get('detail', '')
    tags = request.POST.get('tags', '')
    if (email != '' and title != '' and detail != '' and tags != ''):
        add_new_question_to_database(request, title, detail, tags, email)
        return HttpResponseRedirect('/') 
    return render(request, 'overflow/post.html')

def add_new_question_to_database(request, title, detail, tags, email):
    q = Question(author = email, question_title = title, question_detail = detail, tags = tags, pub_date = timezone.now(), status = 'unsolved')
    q.save()
    print "question added"


def add_comment_to_question(request, question, text, email):
    c = Comment(question=question, comment_text=text, author=email, pub_date=timezone.now())
    c.save()

def upvote_object (request, target):
    target.upvotes += 1

def downvote_object (request, target):
    target.downvotes += 1