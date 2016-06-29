from django.contrib.auth.models import User
# from django import forms

def check_and_register_user(form):
        if form.is_valid():
            # check if the passwords match
            if not form.cleaned_data['password'] == form.cleaned_data['confirm_password']:
                return 1
                # raise forms.ValidationError("Your Password Does Not Match the Confirmation")

            # check if the user already exists
            try:
                User.objects.get(username__iexact=form.cleaned_data['username'])
                return 2
            except User.DoesNotExist:
                # cool, doesn't exist yet
                pass

            User.objects.create_user(first_name=form.cleaned_data['first_name'], \
                                            last_name=form.cleaned_data['last_name'], \
                                            username=form.cleaned_data['username'], \
                                            email=form.cleaned_data['email'], \
                                            password=form.cleaned_data['password'])

            return 0
        return 3

