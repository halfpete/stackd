from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
# from controllers.answer_comments import add_comment_to_answer
from controllers.answers import add_answer_to_question
from controllers.answercomments import add_comment_to_answer
from controllers.questioncomments import add_comment_to_question
from controllers.questions import add_new_question_to_database
from controllers.register import check_and_register_user
from controllers.login import log_user_in, log_user_out
from controllers.comments import downvote
from .models import Question, Comment, AnswerComment, Answer
# from django.utils import timezone
from django.template import loader, RequestContext
# from django.db import connection
# from django.contrib.auth import authenticate, login

from .forms import LoginForm, RegisterForm

# from django import forms

register_errors = ["Indicates Successful Login, never reached", "Your password and confirmation did not match", "That Username already exists",\
                   "There was an error in the form data"]


def index(request):
    question_list = Question.objects.order_by('-pub_date')
    template = loader.get_template('overflow/index.html')
    context = {
        'question_list': question_list,
    }
    return HttpResponse(template.render(context, request))

def thumbup_question(request, question_id):
    question = Question.objects.get(id = question_id)
    upvote_object(request, question)
    question.save()
    return HttpResponseRedirect('/%s/' %(question.id))

def thumbdown_question(request, question_id):
    question = Question.objects.get(id = question_id)
    downvote_object(request, question)
    question.save()
    return HttpResponseRedirect('/%s/' %(question.id))

def thumbup_comment(request, comment_id):
    comment = Comment.objects.get(id = comment_id)
    upvote_object(request, comment)
    comment.save()
    question = comment.question.id
    return HttpResponseRedirect('/%s/' %(question))

def thumbdown_comment(request, comment_id):
    comment = Comment.objects.get(id = comment_id)
    downvote_object(request, comment)
    comment.save()
    question = comment.question.id
    return HttpResponseRedirect('/%s/' %(question))


def detail(request, question_id):
   question = Question.objects.get(id=question_id)
   username = request.user.username
   new_comment = request.POST.get('comment', '')
   new_answer = request.POST.get('answer', '')

   if username != '' and new_answer != '':
       print "added answer to question"
       add_answer_to_question(request, question, new_answer, username)
   answer_list = question.answer_set.order_by('upvotes')


   if username != '' and new_comment != '':
       add_comment_to_question(request, question, new_comment, username)
   comment_list = question.comment_set.order_by('-pub_date')


   list_AnswerComment_list = []

   for answer in answer_list:
       new_answer_comment = request.POST.get('AnswerComment', '')
       if username != '' and new_answer_comment != '':
           add_comment_to_answer(request, answer, new_answer_comment, username)
           # AnswerComment_list = answer.AnswerComment_set.order_by('upvotes')
           list_AnswerComment_list.append(answer.AnswerComment_set.order_by('upvotes'))


   tags = question.tags.split(', ')
   context = {
       'question': question,
       'comment_list': comment_list,
       'answer_list': answer_list,
       # 'AnswerComment_list': AnswerComment_list,
       'list_AnswerComment_list': list_AnswerComment_list,
       'tags': tags
   }
   # upvote = request.POST.get('upvote')
   # downvote = request.POST.get('downvote')

   return render(request, 'overflow/detail.html', context)


def post(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/overflow/login')
    # email = request.POST.get('email_field', '')
    username = request.user.username
    title = request.POST.get('title', '')
    detail = request.POST.get('detail', '')
    tags = request.POST.get('tags', '')
    userID = request.user.pk
    if username != '' and title != '' and detail != '' and tags != '':
        add_new_question_to_database(request, title, detail, tags, username, userID)
        return HttpResponseRedirect('/')
    return render(request, 'overflow/post.html')


def upvote_object(request, target):
    target.upvotes += 1

def downvote_object (request, target):
    target.downvotes += 1


def user_logout(request):
    log_user_out(request)
    return HttpResponseRedirect('/')

def user_login(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/')

    # cobbled from the django tutorials
    if request.method == "POST":
        form = LoginForm(request.POST)

        log_user_in(form, request)

        return HttpResponseRedirect('/')#render(request, 'overflow/login.html', {'form' : form, 'error' : error})
    else:
        form = LoginForm()
        return HttpResponse(render(request, 'overflow/login.html', {'form' : form, 'error' : False}))



def register(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/')
    if request.method == "POST":
        form = RegisterForm(request.POST)

        check_and_register_user(form)

        return HttpResponseRedirect('/login/')#HttpResponse(render(request, 'overflow/register.html', {'form': form, 'error' : error, 'error_msg' : register_errors[error]}))
    else:
        form = RegisterForm()

    return HttpResponse(render(request, 'overflow/register.html', {'form': form, 'error' : False}))
