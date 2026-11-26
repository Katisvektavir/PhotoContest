from service_objects.services import Service
from django import forms
from django.contrib.auth import authenticate


class LoginService(Service):
    username = forms.CharField()
    password = forms.CharField()

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        if username and password:
            user = authenticate( username=username, password=password)
            if user:
                self._user = user
            else:
                raise forms.ValidationError('Неверный логин или пароль')
        return cleaned_data

    def process(self):
        return self._user


