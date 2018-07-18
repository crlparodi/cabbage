from djmoney.models.fields import MoneyField
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone


class User(models.Model):
    JOB_CHOICES = (
        ('CAD', "Cadre"),
        ('CAS', "Cadre Supérieur"),
        ('CAP', "Cadre de la fonction publique"),
        ('AGP', "Agent de production"),
        ('ENS', "Enseignant"),
        ('MFO', "Mère au Foyer"),
        ('RET', "Retraitée"),
    )

    name = models.CharField(
        "Nom",
        max_length=60,
        default=" ",
    )
    age = models.PositiveSmallIntegerField(
        "Âge",
        default=0,
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
        return self.name


class Babysitter(User):
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
        ('DAY', "Toute la journée"),
        ('EV', "Toute la soirée"),
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


