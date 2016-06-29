from overflow.models import AnswerComment
from django.utils import timezone


def add_comment_to_answer(request, answer, text, email):
    c = AnswerComment(question=None, answer=answer, comment_text=text, author=email, pub_date=timezone.now())
    c.save()
    print "comment added to answer"


def upvote(request, question):
    c = AnswerComment.objects.get(question)
    c.upvotes += 1


def downvote(request, question):
    c = AnswerComment.objects.get(question)
    c.downvotes += 1


def get_author(request, question):
    c = AnswerComment.objects.get(question)
    return c.author


def get_netvotes(request, question):
    c = AnswerComment.objects.get(question)
    return c.netvotes()


def get_upvotes(request, question):
    c = AnswerComment.objects.get(question)
    return c.upvotes


def get_downvotes(request, question):
    c = AnswerComment.objects.get(question)
    return c.downvotes


def get_pub_date(request, question):
    c = AnswerComment.objects.get(question)
    return c.pub_date


def get_comment_text(request, question):
    c = AnswerComment.objets.get(question)
    return c.comment_text


def set_pub_date(request, question, new_pubdate):
    q = AnswerComment.objects.get(question)
    q.pub_date = new_pubdate


def set_upvotes(request, question, new_upvotes):
    q = AnswerComment.objects.get(question)
    q.upvotes = new_upvotes


def set_downvotes(request, question, new_downvotes):
    q = AnswerComment.objects.get(question)
    q.downvotes = new_downvotes
