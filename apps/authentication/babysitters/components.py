# coding: utf-8

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
    ('ALL', "Tout âge"),
)

AGE_TARGET_EMPTY = (('', ''), ) + AGE_TARGET_CHOICES

TIME_TARGET_CHOICES = (
    ('AM', "Matin"),
    ('PM', "Après-midi"),
    ('NO', "Soir"),
    ('DI', "Toute la journée"),
)

TIME_TARGET_EMPTY = (('', ''), ) + TIME_TARGET_CHOICES

LOCATIONS = (
    ('AIX', "Aix-en-Provence"),
    ('MAR', "Marseille"),
    ('AVG', "Avignon"),
)

LOCATIONS_EMPTY = (('', ''), ) + LOCATIONS

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