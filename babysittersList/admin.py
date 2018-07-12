from django.contrib import admin
from .models import Babysitter


# Register your models here.

class BabySitterAdmin(admin.ModelAdmin):
    list_display = ('nurse_name', 'birth_location', 'age_target', 'time_target', 'price', 'price_unit')


    fieldsets = (
        ('Situation Personnelle', {
            'fields': (
                'nurse_name',
                'age',
                'birth_location'
            )
        }),
        ('Garde d\'enfants', {
                'fields': (
                'age_target',
                'time_target'
            )
        }),
        ('Parcours professionnel', {
            'fields': (
                'job',
                'grade_main',
                'grade_sec',
                'grade_tri',
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


admin.site.register(Babysitter, BabySitterAdmin)
