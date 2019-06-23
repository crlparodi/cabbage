from apps.authentication.babysitters.models import Babysitter
from apps.authentication.accounts.models import Member
from django import forms
from django.contrib.auth.forms import UserChangeForm

# Getting a custom user model
from django.contrib.auth import get_user_model


class MemberProfileForm(UserChangeForm):
    password = None

    class Meta(UserChangeForm):
        model = get_user_model()
        fields = ('full_name', 'is_babysitter', )
        exclude = ('email', )


class BabysitterProfileForm(forms.ModelForm):
    class Meta:
        model = Babysitter
        fields = '__all__'
        exclude = ('member',)
