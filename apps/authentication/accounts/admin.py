from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Member
from .forms import MemberAdminCreationForm, MemberAdminChangeForm


@admin.register(Member)
class MemberAdmin(BaseUserAdmin):
    search_fields = ('email', 'full_name',)

    list_display = ('email', 'full_name', 'is_active',
                    'is_babysitter', 'creation_date',)
    list_filter = ()

    filter_horizontal = ()
    ordering = ('full_name',)

    form = MemberAdminChangeForm
    add_form = MemberAdminCreationForm

    fieldsets = (
        ('Informations personnelles', {
            'fields': ('email', 'full_name', )
        }),
        ('Mot de passe', {
            'fields': ('password', )
        }),
        ('User authorizations', {
            'fields': ('is_staff', 'admin_profile', )
        })
    )
    add_fieldsets = (
        ('Informations personnelles', {
            'classes': ('wide',),
            'fields': ('email', 'full_name',),
        }),
        ('Mot de passe', {
            'fields': ('password1', 'password2', )
        }),
        ('Ce compte est-il Babysitter ?', {
            'fields': ('is_babysitter', )
        }),
        ('User authorizations', {
            'fields': ('is_staff', 'admin_profile', )
        })
    )


admin.site.unregister(Group)
