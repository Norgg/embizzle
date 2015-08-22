from django.contrib.auth.models import User
from django.forms import CharField, Form, PasswordInput, ValidationError


class RegistrationForm(Form):
    leader_name = CharField()
    password = CharField(widget=PasswordInput())
    repeat_password = CharField(widget=PasswordInput())

    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        if User.objects.filter(username=cleaned_data['leader_name']).count() > 0:
            raise ValidationError("Name taken.")
        elif cleaned_data['password'] != cleaned_data['repeat_password']:
            raise ValidationError("Passwords do not match.")
