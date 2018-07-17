from django.contrib import admin
from .models import User, Babysitter


# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'birth_location', 'age', 'phone', 'email', )

    fieldsets = (
        ('Situation Personnelle', {
            'fields': (
                'name',
                'age',
                'birth_location'
            )
        }),
        ('Parcours professionnel', {
            'fields': (
                'job',
            )
        }),
        ('Contacts', {
            'fields': (
                'phone',
                'email',
            )
        })
    )


class BabySitterAdmin(admin.ModelAdmin):
    list_display = ('name', 'birth_location', 'age_target', 'time_target', 'price', 'price_unit')


    fieldsets = (
        ('Situation Personnelle', {
            'fields': (
                'name',
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


admin.site.register(User, UserAdmin)
admin.site.register(Babysitter, BabySitterAdmin)
