from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from django.views.generic.edit import UpdateView

from apps.authentication.accounts.models import Member
from apps.authentication.babysitters.models import Babysitter

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


"""
def profile_page(request):
    if request.method == 'POST':
        pass 

    if request.method == 'GET':
        pass
"""


class CabbageUserProfileUpdate(UpdateView):
    model = Member
    fields = '__all__'
    exclude = [
        'is_active',
        'is_staff',
        'admin_profile',
        'creation_date',
    ]


class CabbageBabysitterProfileUpdate(UpdateView):
    model = Babysitter
    fields = '__all__'
    exclude = ['member', ]
