from overflow.models import Answer
from django.utils import timezone


def add_answer_to_question(request, question, text, email):
    a = Answer(question=question, answer_text=text, author=email, pub_date=timezone.now())
    a.save()


def upvote(request, question):
    c = Answer.objects.get(question)
    c.upvotes += 1


def downvote(request, question):
    c = Answer.objects.get(question)
    c.downvotes += 1


def get_author(request, question):
    c = Answer.objects.get(question)
    return c.author


def get_netvotes(request, question):
    c = Answer.objects.get(question)
    return c.netvotes()


def get_upvotes(request, question):
    c = Answer.objects.get(question)
    return c.upvotes


def get_downvotes(request, question):
    c = Answer.objects.get(question)
    return c.downvotes


def get_pub_date(request, question):
    c = Answer.objects.get(question)
    return c.pub_date


def get_answer_text(request, question):
    c = Answer.objets.get(question)
    return c.Answer_text


def set_pub_date(request, question, new_pubdate):
    q = Answer.objects.get(question)
    q.pub_date = new_pubdate


def set_upvotes(request, question, new_upvotes):
    q = Answer.objects.get(question)
    q.upvotes = new_upvotes


def set_downvotes(request, question, new_downvotes):
    q = Answer.objects.get(question)
    q.downvotes = new_downvotes
