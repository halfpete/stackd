from overflow.models import Answer_Comment
from django.utils import timezone


def add_comment_to_answer(request, answer, text, email):
    c = Answer_Comment(question=None, answer=answer, comment_text=text, author=email, pub_date=timezone.now())
    c.save()
    print "comment added to answer"


def upvote(request, question):
    c = Answer_Comment.objects.get(question)
    c.upvotes += 1


def downvote(request, question):
    c = Answer_Comment.objects.get(question)
    c.downvotes += 1


def get_author(request, question):
    c = Answer_Comment.objects.get(question)
    return c.author


def get_netvotes(request, question):
    c = Answer_Comment.objects.get(question)
    return c.netvotes()


def get_upvotes(request, question):
    c = Answer_Comment.objects.get(question)
    return c.upvotes


def get_downvotes(request, question):
    c = Answer_Comment.objects.get(question)
    return c.downvotes


def get_pub_date(request, question):
    c = Answer_Comment.objects.get(question)
    return c.pub_date


def get_comment_text(request, question):
    c = Answer_Comment.objets.get(question)
    return c.comment_text


def set_pub_date(request, question, new_pubdate):
    q = Answer_Comment.objects.get(question)
    q.pub_date = new_pubdate


def set_upvotes(request, question, new_upvotes):
    q = Answer_Comment.objects.get(question)
    q.upvotes = new_upvotes


def set_downvotes(request, question, new_downvotes):
    q = Answer_Comment.objects.get(question)
    q.downvotes = new_downvotes
