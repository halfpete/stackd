from django import forms

# XXX: make this common to all files here
MAX_USERNAME_LENGTH = 60

class LoginForm(forms.Form):
    username = forms.CharField(label="Username", max_length=MAX_USERNAME_LENGTH)
    password = forms.CharField(label="Password")


class RegisterForm(forms.Form):
    first_name = forms.CharField(label="First Name", max_length=MAX_USERNAME_LENGTH)
    last_name = forms.CharField(label="Last Name", max_length=MAX_USERNAME_LENGTH)
    username = forms.CharField(label="Username", max_length=MAX_USERNAME_LENGTH)
    email = forms.EmailField(label="E-mail", max_length=MAX_USERNAME_LENGTH)
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    confirm_password = forms.CharField(label="Confirm Password", widget=forms.PasswordInput)
