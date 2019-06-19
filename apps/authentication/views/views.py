from django.http.response import HttpResponseRedirect
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView, PasswordResetView, PasswordResetDoneView, PasswordResetCompleteView
from apps.authentication.accounts.forms import CabbageLoginForm, CabbagePasswordChangeForm, CabbagePasswordResetForm, CabbageSetPasswordForm

""" 
LOGIN PAGES 
"""


def cabbage_login_check(request):
    """
        Si l'utilisateur n'est pas connecté, il est redirigé vers la page de login.
        Sinon, retour à l'accueil...
    """
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/accounts/login')
    else:
        return HttpResponseRedirect('/')


class CabbageLoginView(LoginView):
    form_class = CabbageLoginForm
    template_name = 'authentication/login.html'  # CUSTOM TEMPLATE


""" 
LOGOUT PAGES 
"""


class CabbageLogoutView(LogoutView):
    template_name = 'authentication/logged_out.html'  # CUSTOM TEMPLATE


""" 
PASSWORD CHANGE PAGES 
"""


class CabbagePasswordChangeView(PasswordChangeView):
    form_class = CabbagePasswordChangeForm
    template_name = 'authentication/password_change_form.html'  # CUSTOM TEMPLATE


class CabbagePasswordChangeDone(PasswordChangeDoneView):
    template_name = 'authentication/password_change_done.html'  # CUSTOM TEMPLATE


""" 
PASSWORD RESET PAGES 
"""


class CabbagePasswordResetView(PasswordResetView):
    form_class = CabbagePasswordResetForm
    subject_template_name = 'authentication/password_reset_subject.txt'  # CUSTOM TEMPLATE
    template_name = 'authentication/password_reset_form.html'  # CUSTOM TEMPLATE


class CabbagePasswordResetDone(PasswordResetDoneView):
    template_name = 'authentication/password_reset_done.html'  # CUSTOM TEMPLATE


class CabbagePasswordResetConfirm(PasswordResetDoneView):
    form_class = CabbageSetPasswordForm
    template_name = 'authentication/password_reset_done.html'  # CUSTOM TEMPLATE


class CabbagePasswordResetComplete(PasswordResetCompleteView):
    template_name = 'authentication/password_reset_complete.html'  # CUSTOM TEMPLATE
