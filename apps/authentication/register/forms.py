from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

class MemberCreateForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ("email", "full_name", "is_babysitter",)
        field_classes = None