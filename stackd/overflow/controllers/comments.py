from overflow.models import Question


def upvote(request, question, primary_key):
    q = Question.objects.get(primary_key)
    q.upvotes += 1


def downvote(request, question, primary_key):
    q = Question.objects.get(primary_key)
    q.downvotes += 1


def get_netvotes(request, question, primary_key):
    q = Question.objects.get(primary_key)
    return q.netvotes()


def get_upvotes(request, question, primary_key):
    q = Question.objects.get(primary_key)
    return q.upvotes


def get_downvotes(request, question, primary_key):
    q = Question.objects.get(primary_key)
    return q.downvotes


def get_pub_date(request, question, primary_key):
    q = Question.objects.get(primary_key)
    return q.pub_date

def get_Question_text(request, question, primary_key):



def set_pub_date(request, question, primary_key, new_pubdate):
    q = Question.objects.get(primary_key)
    q.pub_date = new_pubdate


def set_upvotes(request, question, primary_key, new_upvotes):
    q = Question.objects.get(primary_key)
    q.upvotes = new_upvotes


def set_downvotes(request, question, primary_key, new_downvotes):
    q = Question.objects.get(primary_key)
    q.downvotes = new_downvotes
