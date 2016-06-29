from overflow.models import Question_Comment
from django.utils import timezone


def add_comment_to_question(request, question, text, email):
    c = Question_Comment(question=question, answer=None, comment_text=text, author=email, pub_date=timezone.now())
    c.save()
    print "comment added to question"


def upvote(request, question):
    c = Question_Comment.objects.get(question)
    c.upvotes += 1


def downvote(request, question):
    c = Question_Comment.objects.get(question)
    c.downvotes += 1


def get_author(request, question):
    c = Question_Comment.objects.get(question)
    return c.author


def get_netvotes(request, question):
    c = Question_Comment.objects.get(question)
    return c.netvotes()


def get_upvotes(request, question):
    c = Question_Comment.objects.get(question)
    return c.upvotes


def get_downvotes(request, question):
    c = Question_Comment.objects.get(question)
    return c.downvotes


def get_pub_date(request, question):
    c = Question_Comment.objects.get(question)
    return c.pub_date


def get_comment_text(request, question):
    c = Question_Comment.objets.get(question)
    return c.comment_text


def set_pub_date(request, question, new_pubdate):
    q = Question_Comment.objects.get(question)
    q.pub_date = new_pubdate


def set_upvotes(request, question, new_upvotes):
    q = Question_Comment.objects.get(question)
    q.upvotes = new_upvotes


def set_downvotes(request, question, new_downvotes):
    q = Question_Comment.objects.get(question)
    q.downvotes = new_downvotes
