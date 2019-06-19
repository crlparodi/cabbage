# accounts.forms.py
from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.forms import ReadOnlyPasswordHashField, AuthenticationForm, PasswordChangeForm, PasswordResetForm, SetPasswordForm
from .models import Member


class RegisterForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Confirm password', widget=forms.PasswordInput)

    class Meta:
        model = Member
        fields = ('email',
                  'full_name',)

    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = Member.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError(
                "Cette adresse mail est déjà utilisée.")
        return email

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                "Les mots de passes ne correspondent pas.")
        return password2


class MemberAdminCreationForm(forms.ModelForm):
    password1 = forms.CharField(
        label="Mot de passe", widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Confirmez votre mot de passe", widget=forms.PasswordInput)

    class Meta:
        model = Member
        fields = ('email', 'full_name', 'is_babysitter', )

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                "Les mots de passes ne correspondent pas.")
        return password2

    def save(self, commit=True):
        # Il s'agit ici de forcer l'enregistrement du mot de passe chiffré
        user = super(MemberAdminCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data.get("password1"))
        if commit:
            user.save()
        return user


class MemberAdminChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        models = Member
        fields = ('email',
                  'full_name',
                  'is_active',
                  'is_staff',
                  'admin_profile',)

    def clean_password(self):
        # L'idée est de renvoyer à l'administrateur, le mot de passe initial
        # peu importe le nouveau mot de passe que rentrera l'utilisateur.
        # C'est une couche de sécurité supplémentaire qui est apportée ici.
        return self.initial['password']


class CabbageLoginForm(AuthenticationForm):
    username = forms.EmailField(
        label="Adresse mail", widget=forms.EmailInput(attrs={'autofocus': True}))
    password = forms.CharField(
        label="Mot de passe", strip=False, widget=forms.PasswordInput)

    class Meta:
        model = Member


class CabbagePasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        label=("Ancien mot de passe"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autofocus': True}),
    )
    new_password1 = forms.CharField(
        label=("Nouveau mot de passe"),
        widget=forms.PasswordInput,
        strip=False,
        help_text=password_validation.password_validators_help_text_html(),
    )
    new_password2 = forms.CharField(
        label=("Confirmation du mot de passe"),
        strip=False,
        widget=forms.PasswordInput,
    )


class CabbagePasswordResetForm(PasswordResetForm):
    pass


class CabbageSetPasswordForm(SetPasswordForm):
    pass
