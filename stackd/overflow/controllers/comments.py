from overflow.models import Comment


def upvote(request, question):
    c = Comment.objects.get(question)
    c.upvotes += 1


def downvote(request, question):
    c = Comment.objects.get(question)
    c.downvotes += 1


def get_author(request, question):
    c = Comment.objects.get(question)
    return c.author


def get_netvotes(request, question):
    c = Comment.objects.get(question)
    return c.netvotes()


def get_upvotes(request, question):
    c = Comment.objects.get(question)
    return c.upvotes


def get_downvotes(request, question):
    c = Comment.objects.get(question)
    return c.downvotes


def get_pub_date(request, question):
    c = Comment.objects.get(question)
    return c.pub_date


def get_comment_text(request, question):
    c = Comment.objets.get(question)
    return c.comment_text


def set_pub_date(request, question, new_pubdate):
    q = Comment.objects.get(question)
    q.pub_date = new_pubdate


def set_upvotes(request, question, new_upvotes):
    q = Comment.objects.get(question)
    q.upvotes = new_upvotes


def set_downvotes(request, question, new_downvotes):
    q = Comment.objects.get(question)
    q.downvotes = new_downvotes
