from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils import timezone


class MemberManager(BaseUserManager):
    def create_member(self, email, full_name, password=None, is_babysitter=False, is_active=True, is_staff=False, is_admin=False):
        if not email:
            raise ValueError("Une adresse mail est requise.")
        if not full_name:
            raise ValueError("Une nom et prénom sont requis.")
        if not password:
            raise ValueError("Une mot de passe est requis.")

        member_obj = self.model(
            email=self.normalize_email(email),
            full_name=full_name,
        )
        member_obj.set_password(password)
        member_obj.babysitter = is_babysitter
        member_obj.active_profile = is_active
        member_obj.staff_profile = is_staff
        member_obj.admin_profile = is_admin
        member_obj.save(using=self._db)
        return member_obj

    def create_babysitter_user(self, email, full_name, password=None):
        babysitter_obj = self.create_member(email, full_name, password=password, is_babysitter=True)
        return babysitter_obj

    def create_staff_user(self, email, full_name, password=None):
        staff_obj = self.create_member(email, full_name, password=password, is_staff=True)
        return staff_obj

    def create_superuser(self, email, full_name, password=None):
        su_obj = self.create_member(email, full_name, password=password, is_staff=True, is_admin=True)
        return su_obj


class Member(AbstractBaseUser):

    # Base user profile settings (MANDATORY - OBLIGATOIRE)
    email = models.EmailField(verbose_name='Adresse Mail', max_length=255, unique=True)
    full_name = models.CharField(verbose_name='Nom et Prénom', max_length=255)

    # Account set as Babysitter Profile
    babysitter = models.BooleanField(verbose_name="Compte Babysitter", default=False)

    # User profile authorizations
    active_profile = models.BooleanField(verbose_name='Actif', default=True)
    staff_profile = models.BooleanField(verbose_name='Staff', default=False)
    admin_profile = models.BooleanField(verbose_name='Administrateur', default=False)
    creation_date = models.DateField(verbose_name='Date de création', default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name', ]

    objects = MemberManager()

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
    def is_babysitter(self):
        return self.babysitter

    @property
    def is_active(self):
        return self.active_profile

    @property
    def is_staff(self):
        return self.staff_profile

    @property
    def is_admin(self):
        return self.admin_profile

    class Meta:
        verbose_name = "Membre"
        verbose_name_plural = "Membres"
