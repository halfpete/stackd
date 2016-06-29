from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from controllers.answer_comments import add_comment_to_answer
from controllers.answers import add_answer_to_question
from controllers.question_comments import add_comment_to_question
from controllers.questions import add_new_question_to_database
from .models import Question, AnswerComment, Comment, Answer
from django.utils import timezone
from django.template import loader, RequestContext
from django.db import connection
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

from .forms import LoginForm, RegisterForm

from django import forms


def index(request):
    question_list = Question.objects.order_by('-pub_date')
    template = loader.get_template('overflow/index.html')
    context = {
        'question_list': question_list,
    }
    return HttpResponse(template.render(context, request))


def detail(request, question_id):
   question = Question.objects.get(id=question_id)
   email = request.POST.get('email_field', '')
   new_comment = request.POST.get('comment', '')

   if email != '' and new_comment != '':
       add_comment_to_question(request, question, new_comment, email)
   comment_list = question.comment_set.order_by('-pub_date')
   answer = question.answer_set.order_by('upvotes')
   context = {
       'question': question,
       'comment_list': comment_list,
       'answer': answer
   }

   answer_email = request.POST.get('answer_email', '')
   answer_text = request.POST.get('answer_text', '')
   if answer_email != '' and answer_text != '':
       print "added answer to question"
       add_answer_to_question(request, question, answer_text, answer_email)


   upvote = request.POST.get('upvote')
   downvote = request.POST.get('downvote')

   return render(request, 'overflow/detail.html', context)


def post(request):
    email = request.POST.get('email_field', '')
    title = request.POST.get('title', '')
    detail = request.POST.get('detail', '')
    tags = request.POST.get('tags', '')
    userID = request.user.pk
    if email != '' and title != '' and detail != '' and tags != '':
        add_new_question_to_database(request, title, detail, tags, email, userID)
        return HttpResponseRedirect('/')
    return render(request, 'overflow/post.html')


def upvote_object(request, target):
    target.upvotes += 1

def downvote_object (request, target):
    target.downvotes += 1


def user_login(request):

    # cobbled from the django tutorials
    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])

            if  user and user.is_active:
                login(request, user)

            else:
                return render(request, 'overflow/login.html', {'form' : None, 'error' : True})

        else:
            return render(request, 'overflow/login.html', {'form' : None, 'error' : True})

    else:
        form = LoginForm()

    return HttpResponse(render(request, 'overflow/login.html', {'form' : form, 'error' : False}))



def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            # check if the passwords match
            if not form.cleaned_data['password'] == form.cleaned_data['confirm_password']:
                raise forms.ValidationError("Your Password Does Not Match the Confirmation")
                # return render(request, 'overflow/register', {'form' : form, 'error' : True})

            # check if the user already exists
            try:
                User.objects.get(username__iexact=form.cleaned_data['username'])
                raise forms.ValidationError("That Username already exists")
            except User.DoesNotExist:
                # cool, doesn't exist yet
                pass

            User.objects.create_user(first_name=form.cleaned_data['first_name'], \
                                            last_name=form.cleaned_data['last_name'], \
                                            username=form.cleaned_data['username'], \
                                            email=form.cleaned_data['email'], \
                                            password=form.cleaned_data['password'])

            return HttpResponse(render(request, 'overflow/register.html', {'form': form, 'error' : False}))
        else:
            return HttpResponse(render(request, 'overflow/register.html', {'form': None, 'error' : True}))
    else:
        form = RegisterForm()

    return HttpResponse(render(request, 'overflow/register.html', {'form': form, 'error' : False}))
