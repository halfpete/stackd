from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from controllers.answer_comments import add_comment_to_answer
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
    context = {
        'question': question,
        'comment_list': comment_list,
    }

    upvote = request.POST.get('upvote')
<<<<<<< HEAD
    # downvote = request.POST.get('downvote')
    if (upvote != None):
=======
    downvote = request.POST.get('downvote')
    if upvote != None:
>>>>>>> d44a7902ac108174dd9b4cc1830d3f7014976b0c
        upvote_object(request, )

    return render(request, 'overflow/detail.html', context)


def post(request):
    email = request.POST.get('email_field', '')
    title = request.POST.get('title', '')
    detail = request.POST.get('detail', '')
    tags = request.POST.get('tags', '')
    if email != '' and title != '' and detail != '' and tags != '':
        add_new_question_to_database(request, title, detail, tags, email)
        return HttpResponseRedirect('/')
    return render(request, 'overflow/post.html')


# def add_new_question_to_database(request, title, detail, tags, email):
#     q = Question(author=email, question_title=title, question_detail=detail, tags=tags, pub_date=timezone.now(),
#                  status='unsolved')
#     q.save()
#     print "question added"
#
#
# def add_comment_to_question(request, question, text, email):
#     c = Comment(question=question, comment_text=text, author=email, pub_date=timezone.now())
#     c.save()
#
#
# def add_comment_to_answer(request, answer, text, email):
#     c = Comment(answer=answer, comment_text=text, author=email, pub_date=timezone.now())
#     c.save()
#
#
# def add_answer_to_question(request, question, text, email):
#     a = Answer(question=question, answer_text=text, author=email, pub_date=timezone.now())
#     a.save()


def upvote_object(request, target):
    target.upvotes += 1

<<<<<<< HEAD
def downvote_object (request, target):
    target.downvotes += 1



def user_login(request):

    # cobbled from the django tutorials
    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])

            if user.is_active:
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

def downvote_object(request, target):
    target.downvotes += 1
