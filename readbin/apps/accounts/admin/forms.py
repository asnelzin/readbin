from django import forms
from django.contrib.auth.admin import UserChangeForm as BaseUserChangeForm

from rest_framework.authtoken.models import Token
from readbin.apps.accounts.models import User


class UserChangeForm(BaseUserChangeForm):
    token_key = forms.CharField(max_length=40, widget=forms.TextInput(attrs={'size': '40'}))

    class Meta:
        model = User
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(UserChangeForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            self.initial['token_key'] = Token.objects.get(user=instance).key
            self.fields['token_key'].widget.attrs['readonly'] = True
