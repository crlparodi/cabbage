from django.db import models
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver

# Models and Custom Search Components from project
from accounts.models import Member
from babysitters import components

# Fields from third-party Django Components
from djmoney.models.fields import MoneyField
from phonenumber_field.modelfields import PhoneNumberField


# Babysitter Model
class Babysitter(models.Model):

    # Link from Member User Model
    member = models.OneToOneField(Member, on_delete=models.CASCADE, null=True, related_name="babysitter_profile", verbose_name="Membre")

    # Personnal infos (MANDATORY - OBLIGATOIRE)
    location = models.CharField(verbose_name="Ville et environs", max_length=4, choices=components.LOCATIONS, null=False, )
    criminal_record = models.BooleanField(verbose_name="Casier Judiciaire (B1/B2) vierge", default=False, )

    # Other personnal informations
    birth_date = models.DateField(verbose_name="Date de naissance", blank=True, default="1901-01-01")
    grade_main = models.CharField(verbose_name="Premier diplôme", max_length=4, choices=components.GRADES_CHOICES, blank=True, )
    grade_sec = models.CharField(verbose_name="Deuxième diplôme", max_length=4, choices=components.GRADES_CHOICES, blank=True, )
    aid_certificate_grade = models.BooleanField(verbose_name="Brevet de secourisme", default=False, )

    # Babysitting spécificities
    age_target = models.CharField(verbose_name="Tranche d'âge de l'enfant", max_length=4, choices=components.AGE_TARGET_CHOICES, blank=True, )
    time_target = models.CharField(verbose_name="Moments de la journée", max_length=4, choices=components.TIME_TARGET_CHOICES, blank=True, )

    # Service count
    price = MoneyField(verbose_name="Tarifs de vos prestations", max_digits=10, decimal_places=2, default_currency='EUR', )
    price_unit = models.CharField(verbose_name="par", max_length=4, choices=components.TARIFICATION_UNIT, default='H', )

    # Contacts
    phone = PhoneNumberField("Numéro de téléphone", blank=True, )
    linkedin = models.URLField(verbose_name="Profil LinkedIn", blank=True, )
    viadeo = models.URLField(verbose_name="Profil Viadeo", blank=True, )

    class Meta:
        # Rebranding the Model for Administration Site
        verbose_name = 'Babysitter'
        verbose_name_plural = "Babysitters"

    def __str__(self):
        return self.member.__str__()


# Create and setup empty Babysitter Profile,
# only if the 'babysitter' attribute is True during the registration
@receiver(post_save, sender=Member)
def create_babysitter_profile(sender, **kwargs):
    if kwargs['created']:
        if kwargs['instance'].babysitter is True:
            Babysitter.objects.create(member=kwargs['instance'])


# Setting up the Member account if the Babysitter profile is deleted
@receiver(pre_delete, sender=Babysitter)
def remove_babysitter_profile(sender, **kwargs):
    if kwargs['instance'].member.babysitter is True:
        kwargs['instance'].member.babysitter = False
        kwargs['instance'].member.save()


# Setting up the Member account if the Babysitter profile is created
@receiver(post_save, sender=Babysitter)
def setup_member_related_profile(sender, **kwargs):
    kwargs['instance'].member.babysitter = True
    kwargs['instance'].member.save()