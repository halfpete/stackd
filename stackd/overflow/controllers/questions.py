from django.utils import timezone
from overflow.models import Question
from .tag import get_name


def add_new_question_to_database(request, title, detail, tags, email, userID):
    q = Question(question_title=title, question_detail=detail, tags=tags, author=email, pub_date=timezone.now(),
                 status='unsolved', userID=userID)
    q.save()


def upvote(request, question_id):
    q = Question.objects.get(id=question_id)
    q.upvotes += 1


def downvote(request, question_id):
    q = Question.objects.get(id=question_id)
    q.downvotes += 1


def get_author(request, question_id):
    q = Question.objects.get(id=question_id)
    return q.author


def get_netvotes(request, question_id):
    q = Question.objects.get(id=question_id)
    return q.netvotes()


def get_upvotes(request, question_id):
    q = Question.objects.get(id=question_id)
    return q.upvotes


def get_downvotes(request, question_id):
    q = Question.objects.get(id=question_id)
    return q.downvotes


def get_details(request, question_id):
    q = Question.objects.get(id=question_id)
    return q.details


def get_pub_date(request, question_id):
    q = Question.objects.get(id=question_id)
    return q.pub_date


def get_title(request, question_id):
    q = Question.objects.get(id=question_id)
    return q.title


def get_status(request, question_id):
    q = Question.objects.get(id=question_id)
    return q.status


def set_pub_date(request, question_id, new_pubdate):
    q = Question.objects.get(id=question_id)
    q.pub_date = new_pubdate


def set_upvotes(request, question_id, new_upvotes):
    q = Question.objects.get(id=question_id)
    q.upvotes = new_upvotes


def set_downvotes(request, question_id, new_downvotes):
    q = Question.objects.get(id=question_id)
    q.downvotes = new_downvotes


def set_details(request, question_id, new_details):
    q = Question.objects.get(id=question_id)
    q.question_detail = new_details


def set_title(request, question_id, new_title):
    q = Question.objects.get(id=question_id)
    q.question_title = new_title


def set_status(request, question_id, new_status):
    q = Question.objects.get(id=question_id)
    q.status = new_status

