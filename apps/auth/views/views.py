from django.contrib import messages
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic.edit import UpdateView, CreateView


# Import Member and Babysitter Models
from apps.auth.accounts.models import Member
from apps.auth.babysitters.models import Babysitter

# Import Member and Babysitter Profile Page Forms
from apps.auth.accounts_mgmt import forms

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


class ProfileUpdateView(UpdateView):
    model = get_user_model()
    template_name = '/accounts/profile.html'

    # Reception de la page de profil
    def get(self, request, *args, **kwargs):
        # Récupération des données du profil Membre
        member_form = forms.MemberProfileForm(instance=request.user)

        # Si le Membre s'est bien déclaré comme étant un Babysitter, on affiche aussi son profil
        if request.user.is_babysitter is True:
            # Récupération de l'objet
            babysitter = Babysitter.objects.get(member_id=request.user.id)
            # Récupération des données
            babysitter_form = forms.BabysitterProfileForm(instance=babysitter)
        else:
            babysitter_form = None
            babysitter = None

        context = {'babysitter': babysitter, 'babysitter_form': babysitter_form,
                   'member': request.user, 'member_form': member_form}

        return render(request, 'accounts/profile.html', context)

    def post(self, request, *args, **kwargs):
        member_form = forms.MemberProfileForm(request.POST)
        babysitter_form = forms.BabysitterProfileForm(request.POST)

        if member_form.is_valid():
            # Si l'action suivante n'est pas réalisée, il affiche une erreur d'intégration :
            # UNIQUE contraint fail : accounts_member.email
            # Cela implique que l'émail existe déjà, alors qu'on cherche à mettre à jour le profil correspondant,
            # ce qui est hérétique.
            # Il s'agit donc de ne mettre à jour que les données qui nous intéressent.
            instance = member_form.save(commit=False)
            member = request.user
            member.full_name = instance.full_name
            member.is_babysitter = instance.is_babysitter
            member.save()

            # Si l'utilisateur veut créer un profil Babysitter, il peut le faire.
            if instance.is_babysitter is True and not Babysitter.objects.filter(member_id=request.user.id):
                Babysitter.objects.create(member_id = request.user.id)

            # On veut ici mettre à jour le profil Babysitter, sur le même principe que les données Membre
            # Car il faut noter que le profil Babysitter est relié au compte (et donc à l'email qui sera tenté d'être
            # mis à jour car c'est tout le profil - Membre et Babysitter - qui sera mis à jour).
            if babysitter_form is not None and babysitter_form.is_valid():
                instance_babysitter = babysitter_form.save(commit=False)
                if member.is_babysitter is True:
                    babysitter = Babysitter.objects.get(member_id=request.user.id)
                    babysitter = self.update_babysitter_fields(babysitter, instance_babysitter)
                    babysitter.save()
                else:
                    Babysitter.objects.get(member_id=request.user.id).delete()
            # Succès de l'envoi
            messages.success(request, "Les changements ont été effectués avec succès.")
            return redirect('/accounts/profile')
        else:
            # Erreur de formulaire
            messages.error(request, "Oups ! Des erreurs se sont produites lors de l'envoi du formulaire.")
            return redirect('/accounts/profile')

    # Fonction de mise à jour des données du profil Babysitter
    def update_babysitter_fields(self, babysitter, instance):
        babysitter.location = instance.location
        babysitter.criminal_record = instance.criminal_record
        babysitter.birth_date = instance.birth_date
        babysitter.grade_main = instance.grade_main
        babysitter.grade_sec = instance.grade_sec
        babysitter.aid_certificate_grade = instance.aid_certificate_grade
        babysitter.age_target = instance.age_target
        babysitter.time_target = instance.time_target
        babysitter.price = instance.price
        babysitter.price_unit = instance.price_unit
        babysitter.phone = instance.phone
        babysitter.linkedin = instance.linkedin
        babysitter.viadeo = instance.viadeo
        return babysitter

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
        member_form = forms.MemberCreateForm()
        context = {'member_form': member_form}
        return render(request, 'accounts/register.html', context)

    def post(self, request, *args, **kwargs):
        member_form = forms.MemberCreateForm(request.POST)

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
