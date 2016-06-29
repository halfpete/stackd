from django.utils import timezone
from overflow.models import Question
from .tag import get_name


def add_new_question_to_database(request, title, detail, tags, email):
    q = Question(question_title=title, question_detail=detail, tags=tags, author=email, pub_date=timezone.now(),
                 status='unsolved')
    q.save()


def upvote(request, primary_key):
    q = Question.objects.get(primary_key)
    q.upvotes += 1


def downvote(request, primary_key):
    q = Question.objects.get(primary_key)
    q.downvotes += 1


def get_author(request, primary_key):
    q = Question.objects.get(primary_key)
    return q.author


def get_netvotes(request, primary_key):
    q = Question.objects.get(primary_key)
    return q.netvotes()


def get_upvotes(request, primary_key):
    q = Question.objects.get(primary_key)
    return q.upvotes


def get_downvotes(request, primary_key):
    q = Question.objects.get(primary_key)
    return q.downvotes


def get_details(request, primary_key):
    q = Question.objects.get(primary_key)
    return q.details


def get_pub_date(request, primary_key):
    q = Question.objects.get(primary_key)
    return q.pub_date


def get_title(request, primary_key):
    q = Question.objects.get(primary_key)
    return q.title


def get_status(request, primary_key):
    q = Question.objects.get(primary_key)
    return q.status


def set_pub_date(request, primary_key, new_pubdate):
    q = Question.objects.get(primary_key)
    q.pub_date = new_pubdate


def set_upvotes(request, primary_key, new_upvotes):
    q = Question.objects.get(primary_key)
    q.upvotes = new_upvotes


def set_downvotes(request, primary_key, new_downvotes):
    q = Question.objects.get(primary_key)
    q.downvotes = new_downvotes


def set_details(request, primary_key, new_details):
    q = Question.objects.get(primary_key)
    q.question_detail = new_details


def set_title(request, primary_key, new_title):
    q = Question.objects.get(primary_key)
    q.question_title = new_title


def set_status(request, primary_key, new_status):
    q = Question.objects.get(primary_key)
    q.status = new_status

