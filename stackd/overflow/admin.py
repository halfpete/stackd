from django.contrib import admin

# Register your models here.
from .models import Question, AnswerComment, QuestionComment, Answer
admin.site.register(Question)
admin.site.register(AnswerComment)
admin.site.register(QuestionComment)
admin.site.register(Answer)
