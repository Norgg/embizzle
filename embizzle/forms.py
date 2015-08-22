from django.forms import CharField, Form, PasswordInput


class RegistrationForm(Form):
    username = CharField()
    password = CharField(widget=PasswordInput())
    repeat_password = CharField(widget=PasswordInput())
