from django.contrib import admin
from .models import User, Babysitter


# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('name',
                    'birth',
                    'birth_location',
                    'phone',
                    'email',
                    'creation_date',
                    )

    fieldsets = (
        ('Situation Personnelle', {
            'fields': (
                'name',
                'birth',
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
    list_display = ('name',
                    'location',
                    'age_target',
                    'time_target',
                    'price',
                    'price_unit',
                    )


    fieldsets = (
        ('Situation Personnelle', {
            'fields': (
                'name',
                'birth',
                'birth_location'
            )
        }),
        ('Garde d\'enfants', {
                'fields': (
                'age_target',
                'time_target',
                'location',
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
        ('Contacts', {
            'fields': (
                'phone',
                'email',
            )
        }),
        ('Réseaux sociaux professionnels', {
            'fields': (
                'linkedin',
            ),
        }),
    )


admin.site.register(User, UserAdmin)
admin.site.register(Babysitter, BabySitterAdmin)
