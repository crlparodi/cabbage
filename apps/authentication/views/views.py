from django.shortcuts import render, redirect
from django.urls import reverse
from django.http.response import HttpResponseRedirect
from django.views.generic import TemplateView
from django.views.generic.edit import UpdateView, CreateView, DeleteView


# Import Member and Babysitter Models
from apps.authentication.accounts.models import Member
from apps.authentication.babysitters.models import Babysitter

# Import Member and Babysitter Profile Page Forms
from apps.authentication.profile import forms
from apps.authentication.register.forms import MemberCreateForm

# User is custom, so i have to get back the right user model
from django.contrib.auth import get_user_model

"""
LOGIN PAGES
"""

# Verify if the user il already connected or not


def cabbage_login_check(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/accounts/login')
    else:
        return HttpResponseRedirect('/')


"""
PROFILE PAGES
"""

# Commentaries to add/update before building Registration Page !!
class ProfileUpdateView(UpdateView):
    model = get_user_model()
    template_name = '/accounts/profile.html'

    def get(self, request, *args, **kwargs):
        member_form = forms.MemberProfileForm(instance=request.user)

        if request.user.is_babysitter is True:
            babysitter = Babysitter.objects.get(member_id=request.user.id)
            babysitter_form = forms.BabysitterProfileForm(instance=babysitter)
        else:
            babysitter_form = None
            babysitter = None

        context = {'babysitter': babysitter, 'babysitter_form': babysitter_form,
                   'accounts': request.user, 'member_form': member_form}

        return render(request, 'accounts/profile.html', context)

    def post(self, request, *args, **kwargs):
        member_form = forms.MemberProfileForm(request.POST)
        babysitter_form = forms.BabysitterProfileForm(request.POST)

        if member_form.is_valid():
            instance = member_form.save(commit=False)
            member = request.user
            member.full_name = instance.full_name
            member.is_babysitter = instance.is_babysitter
            member.save()
            if instance.is_babysitter is True and not Babysitter.objects.filter(member_id=request.user.id):
                Babysitter.objects.create(member_id = request.user.id)
            if babysitter_form is not None and babysitter_form.is_valid():
                instance_babysitter = babysitter_form.save(commit=False)
                if member.is_babysitter is True:
                    babysitter = Babysitter.objects.get(member_id=request.user.id)
                    babysitter.location = instance_babysitter.location
                    babysitter.criminal_record = instance_babysitter.criminal_record
                    babysitter.birth_date = instance_babysitter.birth_date
                    babysitter.grade_main = instance_babysitter.grade_main
                    babysitter.grade_sec = instance_babysitter.grade_sec
                    babysitter.aid_certificate_grade = instance_babysitter.aid_certificate_grade
                    babysitter.age_target = instance_babysitter.age_target
                    babysitter.time_target = instance_babysitter.time_target
                    babysitter.price = instance_babysitter.price
                    babysitter.price_unit = instance_babysitter.price_unit
                    babysitter.phone = instance_babysitter.phone
                    babysitter.linkedin = instance_babysitter.linkedin
                    babysitter.viadeo = instance_babysitter.viadeo
                    babysitter.save()
                else:
                    Babysitter.objects.get(member_id=request.user.id).delete()
            return redirect('/')
        else:
            error = member_form.errors
            return redirect('/accounts/profile')

    def get_context_data(self, *args, **kwargs):
        instance = super().get_context_data(*args, **kwargs)
        if self.request.method == 'POST':
            instance['form'] = forms.MemberProfileForm(instance=self.request.user)

"""
SIGN UP PAGE
"""

class RegistrationView(CreateView):
    model = get_user_model()

    def get(self, request, *args, **kwargs):
        member_form = MemberCreateForm()
        context = {'member_form': member_form}
        return render(request, 'accounts/register.html', context)

    def post(self, request, *args, **kwargs):
        member_form = MemberCreateForm(request.POST)

        if member_form.is_valid():
            member_form.save()

        return redirect('/')

"""
DELETE ACCOUNT PAGE
"""

def delete_account(request):
    if request.method == 'POST':
        Member.objects.get(id=request.user.id).delete()
        return redirect('/')
    else:
        return render(request, 'accounts/delete.html')
