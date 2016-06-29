from django.contrib import admin

# Register your models here.
from .models import Question, Answer_Comment, Question_Comment, Answer
admin.site.register(Question)
admin.site.register(Answer_Comment)
admin.site.register(Question_Comment)
admin.site.register(Answer)
