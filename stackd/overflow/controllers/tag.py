from overflow.models import Tag, Question


def get_name(request, question):
    t = Tag.objects.get(question)
    return t.name


def set_name(request, question, new_name):
    t = Tag.objects.get(question)
    t.name = new_name


def add_tags(request, question, *tag_names):
    q = Question.objects.get(question.pk)
    for tag_name in tag_names:
        q.tags.append(tag_name + ",")
        t = Tag(question=question, name=tag_name)
        t.save()

