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
    if not request.user:
        return HttpResponseRedirect('overflow/login')
    question_list = Question.objects.order_by('-pub_date')
    template = loader.get_template('overflow/index.html')
    context = {
        'question_list': question_list,
    }
    return HttpResponse(template.render(context, request))


def detail(request, question_id):
   question = Question.objects.get(id=question_id)
   username = request.user.username
   new_comment = request.POST.get('comment', '')

   if username != '' and new_comment != '':
       add_comment_to_question(request, question, new_comment, username)
   comment_list = question.comment_set.order_by('-pub_date')
   answer_list = question.answer_set.order_by('upvotes')
   # AnswerComment_list = answer.AnswerComment_set.order_by('upvotes')
   context = {
       'question': question,
       'comment_list': comment_list,
       'answer_list': answer_list
       # 'AnswerComment_list': AnswerComment_list
   }

   answer_text = request.POST.get('answer_text', '')
   if username != '' and answer_text != '':
       print "added answer to question"
       add_answer_to_question(request, question, answer_text, username)

   # new_answer_comment = request.POST.get('answer_comment', '')
   #
   # if username != '' and new_answer_comment != '':
   #     add_comment_to_answer(request, question, new_answer_comment, username)

   # upvote = request.POST.get('upvote')
   # downvote = request.POST.get('downvote')

   return render(request, 'overflow/detail.html', context)


def post(request):
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

    # cobbled from the django tutorials
    if request.method == "POST":
        form = LoginForm(request.POST)

        log_user_in(form, request)

        return HttpResponseRedirect('/')#render(request, 'overflow/login.html', {'form' : form, 'error' : error})
    else:
        form = LoginForm()
        return HttpResponse(render(request, 'overflow/login.html', {'form' : form, 'error' : False}))



def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)

        check_and_register_user(form)

        return HttpResponseRedirect('overflow/login.html')#HttpResponse(render(request, 'overflow/register.html', {'form': form, 'error' : error, 'error_msg' : register_errors[error]}))
    else:
        form = RegisterForm()

    return HttpResponse(render(request, 'overflow/register.html', {'form': form, 'error' : False}))
