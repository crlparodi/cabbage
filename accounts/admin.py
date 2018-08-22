from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Member
from .forms import MemberAdminCreationForm, MemberAdminChangeForm


@admin.register(Member)
class MemberAdmin(BaseUserAdmin):
    search_fields = ('email', 'full_name',)

    list_display = ('email', 'full_name', 'active_profile', 'babysitter', 'creation_date',)
    list_filter = ('active_profile', 'staff_profile', 'admin_profile',)

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
           'fields': ('active_profile', 'staff_profile', 'admin_profile', )
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
            'fields': ('babysitter', )
        }),
        ('User authorizations', {
           'fields': ('active_profile', 'staff_profile', 'admin_profile', )
        })
    )


admin.site.unregister(Group)
