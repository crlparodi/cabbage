from django.apps import apps
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.signals import setting_changed
from django.db import models
from django.dispatch import receiver
from django.utils import timezone
from django.urls import reverse


"""
MEMBER USER CREATION MODEL
"""


class MemberManager(BaseUserManager):
    use_in_migrations = True
    # Member account creation

    def create_member(self, email, full_name, password=None, is_babysitter=False, is_active=True, is_staff=False, is_admin=False):
        if not email:
            raise ValueError("Une adresse mail est requise.")
        if not full_name:
            raise ValueError("Une nom et prénom sont requis.")
        if not password:
            raise ValueError("Une mot de passe est requis.")

        # Member object creation
        member_obj = self.model(
            email=self.normalize_email(email),
            full_name=full_name,
        )
        member_obj.set_password(password)
        member_obj.is_babysitter = is_babysitter
        member_obj.is_active = is_active
        member_obj.is_staff = is_staff
        member_obj.admin_profile = is_admin
        member_obj.save(using=self._db)
        return member_obj

    # Multiple user rights definitions
    def create_babysitter_user(self, email, full_name, password=None):
        babysitter_obj = self.create_member(
            email, full_name, password=password, is_babysitter=True)
        return babysitter_obj

    def create_staff_user(self, email, full_name, password=None):
        staff_obj = self.create_member(
            email, full_name, password=password, is_staff=True)
        return staff_obj

    def create_superuser(self, email, full_name, password=None):
        su_obj = self.create_member(
            email, full_name, password=password, is_staff=True, is_admin=True)
        return su_obj


"""
MEMBER USER MAIN MODEL
"""


class Member(AbstractBaseUser):

    # Base user profile settings (MANDATORY - OBLIGATOIRE)
    email = models.EmailField(
        verbose_name='Adresse Mail', max_length=255, unique=True)
    full_name = models.CharField(verbose_name='Prénom et NOM', max_length=255)

    # Account set as Babysitter Profile
    is_babysitter = models.BooleanField(
        verbose_name="Compte Babysitter", default=False)

    # User profile authorizations
    is_active = models.BooleanField(verbose_name='Actif', default=True)
    is_staff = models.BooleanField(verbose_name='Staff', default=False)
    admin_profile = models.BooleanField(
        verbose_name='Administrateur', default=False)
    creation_date = models.DateField(
        verbose_name='Date de création', default=timezone.now)

    objects = MemberManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name', ]

    def get_full_name(self):
        if not self.full_name:
            return self.email
        return self.full_name

    def get_short_name(self):
        return self.email

    def __str__(self):
        return self.full_name

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def babysitter(self):
        return self.is_babysitter

    @property
    def active(self):
        return self.is_active

    @property
    def staff(self):
        return self.is_staff

    @property
    def admin(self):
        return self.admin_profile

    class Meta:
        verbose_name = "Membre"
        verbose_name_plural = "Membres"

