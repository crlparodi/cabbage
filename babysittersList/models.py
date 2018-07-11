from django.db import models
from django.contrib import admin

class Babysitter(models.Model):
    JOB_CHOICES = (
        ('BLANK', " "),
        ('MF', "Mère au Foyer"),
    )

    AGE_TARGET_CHOICES = (
        ('BLANK', " "),
        ('BBY', "Nouveau né (0 à 10 mois)"),
        ('GBA', "Nourrisson (10 mois à 2 ans)"),
        ('CHI', "Enfants de 2 à 6 ans"),
        ('GCH', "Enfants de 7 à 12 ans"),
        ('TEE', "Enfants de 12 ans et plus"),
    )

    TIME_TARGET_CHOICES = (
        ('BLANK', " "),
        ('AM', "Matin"),
        ('PM', "Après-midi"),
        ('DAY', "Toute la journée"),
        ('EV', "Toute la soirée"),
    )

    GRADES_CHOICES = (
        ('BLANK', " "),
        ('BAF', "BAFA"),
        ('DPE', "Diplôme de petite enfance"),
    )

    TARIFICATION_UNIT = (
        ('H', "Heure"),
        ('DM', "Demi-Journée"),
        ('DAY', "Jour"),
        ('WEE', "Semaine")
    )

    name = models.CharField(max_length=42, name="Nom", default=" ")
    age = models.PositiveSmallIntegerField("Âge", default=0)
    ville = models.CharField(max_length=64, name="Lieu de naissance", default=" ",)
    job = models.CharField(
        name="Profession",
        max_length=4,
        choices=JOB_CHOICES,
        default='BLANK',
    )

    age_target = models.CharField(
        name="Tranche d'âge de l'enfant",
        max_length=4,
        choices=AGE_TARGET_CHOICES,
        default='BLANK',
    )

    time_target = models.CharField(
        name="Moments de la journée",
        max_length=4,
        choices=TIME_TARGET_CHOICES,
        default='BLANK',
    )

    grade_main = models.CharField(
        name="Premier diplôme",
        max_length=4,
        choices=GRADES_CHOICES,
        default='BLANK',
    )

    grade_sec = models.CharField(
        name="2ème diplôme",
        max_length=4,
        choices=GRADES_CHOICES,
        default='BLANK',
    )

    grade_tri = models.CharField(
        name="3ème diplôme",
        max_length=4,
        choices=GRADES_CHOICES,
        default='BLANK',
    )

    aid_certificate_grade = models.BooleanField(
        "Vous êtes titulaire d'un brevet de secourisme ?",
        default=False
    )

    criminal_record = models.BooleanField(
        "J'atteste sur l'honneur et déclare avoir un casier judiciaire (B1 et B2) vierge.\n(Notez toutefois que la famille de l'enfant peut demander une copie de vos deux casiers judiciaires.)",
        default=False
    )

    price = models.IntegerField("Tarifs de vos prestations", default=0)

    price_unit = models.CharField(
        "par",
        max_length=4,
        choices=TARIFICATION_UNIT,
        default='H',
    )



