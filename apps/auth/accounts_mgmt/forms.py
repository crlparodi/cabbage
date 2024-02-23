from apps.auth.babysitters.models import Babysitter
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserChangeForm

# Getting a custom user model
from django.contrib.auth import get_user_model


class MemberCreateForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ("email", "full_name", "is_babysitter",)
        field_classes = None

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
