from django.contrib import admin
from .models import BabySitter


# Register your models here.

class BabySitterAdmin(admin.ModelAdmin):
    list_display = ('Nom', 'Lieu de naissance', 'Tranche d\'âge de l\'enfant', 'Moments de la journée', 'price', 'price_unit')


    fieldsets = (
        ('Situation Personnelle', {
            'fields': (
                'Nom',
                'age',
                'Lieu de naissance'
            )
        }),
        ('Garde d\'enfants', {
                'fields': (
                'Tranche d\'âge de l\'enfant',
                'Moments de la journée'
            )
        }),
        ('Parcours professionnel', {
            'fields': (
                'Profession',
                'Premier diplôme',
                '2ème diplôme',
                '3ème diplôme',
                'aid_certificate_grade'
            )
        }),
        ("Volet Judiciaire", {
            'fields': (
                "criminal_record",
            )
        }),
        ("Tarification des services", {
            'fields': (
                ('price', 'price_unit'),
            )
        }),
    )


admin.site.register(BabySitter, BabySitterAdmin)
