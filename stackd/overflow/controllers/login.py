# from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

def log_user_in(form, request):
    if form.is_valid():
        user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])

        if  user and user.is_active:
            login(request, user)
            return True
        else:
            return False

def log_user_out(request):
    logout(request)
