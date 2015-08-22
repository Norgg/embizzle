from django.contrib.auth.models import User
from django.forms import CharField, Form, PasswordInput, ValidationError


class RegistrationForm(Form):
    username = CharField()
    leader_name = CharField()
    civilisation_name = CharField()
    password = CharField(widget=PasswordInput())
    repeat_password = CharField(widget=PasswordInput())

    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        if User.objects.filter(username=cleaned_data['username']).count() > 0:
            raise ValidationError("Username taken.")
        elif cleaned_data['password'] != cleaned_data['repeat_password']:
            raise ValidationError("Passwords do not match.")
