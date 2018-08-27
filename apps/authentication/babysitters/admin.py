from django.contrib import admin
from .models import Babysitter
from .forms import BabysitterAdminCreateForm, BabysitterAdminChangeForm


@admin.register(Babysitter)
class BabysitterAdmin(admin.ModelAdmin):
    member = 'member'
    list_display = (member, 'location', 'birth_date', 'age_target', 'time_target', 'phone', )

    add_form = BabysitterAdminCreateForm
    change_form = BabysitterAdminChangeForm

    add_fieldsets = (
        ('Membre concerné', {
            'fields': ('member', 'birth_date', ),
        }),
        ('Parcours scolaire et professionnel', {
            'fields': ('grade_main', 'grade_sec', 'aid_certificate_grade', )
        }),
        ('Volet Judiciaire', {
            'fields': ('criminal_record_attribute', )
        }),
        ("Informations relatives à la garde d'enfant", {
            'fields': ('location', 'age_target', 'time_target', ),
        }),
        ("Tarification de la garde", {
            'fields': (('price', 'price_unit', ), )
        }),
        ('Contacts', {
            'fields': ('phone', 'linkedin', 'viadeo', )
        }),
    )
    change_fieldsets = (
        (None, {
            'fields': ('birth_date', ),
        }),
        ('Parcours scolaire et professionnel', {
            'fields': ('grade_main', 'grade_sec', 'aid_certificate_grade', )
        }),
        ("Informations relatives à la garde d'enfant", {
            'fields': ('location', 'age_target', 'time_target', ),
        }),
        ("Tarification de la garde", {
            'fields': (('price', 'price_unit', ), )
        }),
        ('Contacts', {
            'fields': ('phone', 'linkedin', 'viadeo', )
        }),
    )

    def get_form(self, request, obj=None, change=False, **kwargs):
        if obj is None:
            self.form = self.add_form
            self.fieldsets = self.add_fieldsets
        if obj is not None:
            self.form = self.change_form
            self.fieldsets = self.change_fieldsets
        return super(BabysitterAdmin, self).get_form(request, obj, **kwargs)

    # The following method is overrided to display dynamically the name of the Babysitter
    def render_change_form(self, request, context, add=False, change=False, form_url='', obj=None):
        # self.model is pointing for the model type Babysitter
        # obj is pointing to the babysitter instance
        form_view = super(BabysitterAdmin, self).render_change_form(request, context, add, change, form_url, obj)
        form_view.context_data['title'] = obj.member.full_name if form_view.context_data['object_id'] else "Babysitter Object"
        return form_view
