from overflow.models import Tag


def get_name(request, primary_key):
    t = Tag.objects.get(primary_key)
    return t.name

def set_name(request, primary_key, new_name):
    t = Tag.objects.get(primary_key)
    t.name = new_name
