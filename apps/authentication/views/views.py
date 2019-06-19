from django.http.response import HttpResponseRedirect
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView
from apps.authentication.accounts.forms import CabbagePasswordChangeForm, CabbageLoginForm


def cabbage_login_check(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/accounts/login')
    else:
        return HttpResponseRedirect('/')


class CabbageLoginView(LoginView):
    form_class = CabbageLoginForm
    template_name = 'authentication/login.html'


class CabbageLogoutView(LogoutView):
    template_name = 'authentication/logged_out.html'


class CabbagePasswordChangeView(PasswordChangeView):
    form_class = CabbagePasswordChangeForm
    template_name = 'authentication/password_change_form.html'
    title = 'Changement de mot de passe'


class CabbagePasswordChangeDone(PasswordChangeDoneView):
    template_name = 'authentication/password_change_done.html'
