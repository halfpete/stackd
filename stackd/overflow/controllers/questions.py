# .models import Question, Comment


from django.utils import timezone
from stackd.overflow.models import Question


def add_new_question_to_database(request, title, detail, tags, email):
    q = Question(question_title=title, question_detail=detail, tags=tags, author=email, pub_date=timezone.now(),
                 status='unsolved')
    q.save()
