# coding: utf-8

from djmoney.models.fields import MoneyField
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone
from django import forms

JOB_CHOICES = (
    ('CAD', "Cadre"),
    ('CAS', "Cadre Supérieur"),
    ('CAP', "Cadre de la fonction publique"),
    ('AGP', "Agent de production"),
    ('ENS', "Enseignant"),
    ('MFO', "Mère au Foyer"),
    ('RET', "Retraitée"),
)

AGE_TARGET_CHOICES = (
    ('BBY', "Nouveau né (0 à 10 mois)"),
    ('GBA', "Nourrisson (10 mois à 2 ans)"),
    ('CHI', "Enfants de 2 à 6 ans"),
    ('GCH', "Enfants de 7 à 12 ans"),
    ('TEE', "Enfants de 12 ans et plus"),
)

TIME_TARGET_CHOICES = (
    ('AM', "Matin"),
    ('PM', "Après-midi"),
    ('NO', "Soir"),
    ('DI', "Toute la journée"),
)

LOCATIONS = (
    ('AIX', "Aix-en-Provence"),
    ('MAR', "Marseille"),
    ('AVG', "Avignon"),
)

GRADES_CHOICES = (
    ('BAF', "BAFA"),
    ('DPE', "Diplôme de petite enfance"),
)

TARIFICATION_UNIT = (
    ('TU1', "Heure"),
    ('TU2', "Demi-Journée"),
    ('TU3', "Jour"),
    ('TU4', "Semaine")
)

class User(models.Model):

    """Classe User contenant les informations liées au compte utilisateur.
    Ce dernier peut très bien devenir prémium grâce à un abonnement, ou bien Babysitter et lancer son activité.

    Attributes:
        name        Nom de l'Utilisateur
        age         Age de l'utilisateur (à retirer...)
        birth       Date de naissance de l'utilisateur
        birth_location  Lieu de naissance de l'utilisateur
        job         Métier exercé par l'utilisateur
        phone       Numéro de téléphone de l'utilisateur
        mail        Adresse mail de l'utilisateur
        creation_date   Date de création du compte
    """
    name = models.CharField(
        "Nom",
        max_length=60,
        default=" ",
    )

    birth = models.DateField(
        "Date de naissance",
        max_length=8,
        default=timezone.now,
    )
    birth_location = models.CharField(
        "Lieu de naissance",
        max_length=64,
        blank=True,
    )
    job = models.CharField(
        "Profession",
        max_length=4,
        choices=JOB_CHOICES,
        blank=True,
    )
    phone = PhoneNumberField(
        "Numéro de téléphone",
        blank=True,
    )
    email = models.EmailField(
        "Adresse électronique",
        default=" ",
    )
    creation_date = models.DateTimeField(
        default=timezone.now,
    )

    def __str__(self):
        """Affichage du nom de l'utilisateur crée"""
        return self.name


class Babysitter(User):

    """Classe Babysitter liée à User, contenant les informations relatives à la personne
    dans le cadre de l'exercice de babysitting.

    Attributes:
        age_target      Tranche d'âge de l'enfant à garder.
        time_target     Disponibilité de garde de(s) l'enfant(s)
        location        Lieu de garde de(s) l'enfant(s)
        grade_main      Dernier diplôme obtenu par le babysitter
        grade_sec       Avant-dernier diplôme obtenu par le babysitter
        grade_tri       Troisième diplôme significatif
        aid_certificate_grade   Brevet de secourisme obtenu (ou non) par le babysitter
        criminal_record     Le babysitter atteste de l'absence de casier judiciaire à son égard
        price           Tarification de la garde de(s) l'enfant(s)
        price_unit      Unité temporelle de tarification
        linkedin        Profil LinkedIn du baysitter
    """
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        parent_link=True,
    )

    age_target = models.CharField(
        "Tranche d'âge de l'enfant",
        max_length=4,
        choices=AGE_TARGET_CHOICES,
        blank=True,
    )

    time_target = models.CharField(
        "Moments de la journée",
        max_length=4,
        choices=TIME_TARGET_CHOICES,
        blank=True,
    )

    location = models.CharField(
        "Ville et environs",
        max_length=4,
        choices=LOCATIONS,
        blank=True,
    )

    grade_main = models.CharField(
        "Premier diplôme (Si vous en disposez)",
        max_length=4,
        choices=GRADES_CHOICES,
        blank=True,
    )

    grade_sec = models.CharField(
        "2ème diplôme (Si vous en disposez)",
        max_length=4,
        choices=GRADES_CHOICES,
        blank=True,
    )

    grade_tri = models.CharField(
        "3ème diplôme (Si vous en disposez)",
        max_length=4,
        choices=GRADES_CHOICES,
        blank=True,
    )

    aid_certificate_grade = models.BooleanField(
        "Vous êtes titulaire d'un brevet de secourisme ?",
        default=False,
    )

    criminal_record = models.BooleanField(
        "J'atteste sur l'honneur et déclare avoir un casier judiciaire (B1 et B2) vierge.\n(Notez toutefois que la famille de l'enfant peut demander une copie de vos deux casiers judiciaires.)",
        default=False,
    )

    price = MoneyField(
        "Tarifs de vos prestations",
        max_digits=10,
        decimal_places=2,
        default_currency='EUR',
    )

    price_unit = models.CharField(
        "par",
        max_length=4,
        choices=TARIFICATION_UNIT,
        default='H',
    )

    linkedin = models.URLField(
        "Profil LinkedIn",
        blank=True,
    )


class SearchForm(forms.Form):
    form_name = forms.CharField(
        label="Nom du babysitter",
        max_length=100,
    )

    form_age_target = forms.MultipleChoiceField(
        label="Tranche d'Âge",
        widget=forms.Select,
        choices=AGE_TARGET_CHOICES,
    )

    form_time_target = forms.MultipleChoiceField(
        label="Disponibilité",
        widget=forms.Select,
        choices=TIME_TARGET_CHOICES,
    )

    form_location = forms.MultipleChoiceField(
        label="Ville",
        widget=forms.Select,
        choices=LOCATIONS,
    )
