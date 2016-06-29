from overflow.models import QuestionComment
from django.utils import timezone


def add_comment_to_question(request, question, text, email):
    c = QuestionComment(question=question, answer=None, comment_text=text, author=email, pub_date=timezone.now())
    c.save()
    print "comment added to question"


def upvote(request, question):
    c = QuestionComment.objects.get(question)
    c.upvotes += 1


def downvote(request, question):
    c = QuestionComment.objects.get(question)
    c.downvotes += 1


def get_author(request, question):
    c = QuestionComment.objects.get(question)
    return c.author


def get_netvotes(request, question):
    c = QuestionComment.objects.get(question)
    return c.netvotes()


def get_upvotes(request, question):
    c = QuestionComment.objects.get(question)
    return c.upvotes


def get_downvotes(request, question):
    c = QuestionComment.objects.get(question)
    return c.downvotes


def get_pub_date(request, question):
    c = QuestionComment.objects.get(question)
    return c.pub_date


def get_comment_text(request, question):
    c = QuestionComment.objets.get(question)
    return c.comment_text


def set_pub_date(request, question, new_pubdate):
    q = QuestionComment.objects.get(question)
    q.pub_date = new_pubdate


def set_upvotes(request, question, new_upvotes):
    q = QuestionComment.objects.get(question)
    q.upvotes = new_upvotes


def set_downvotes(request, question, new_downvotes):
    q = QuestionComment.objects.get(question)
    q.downvotes = new_downvotes
