from django import forms

from .models import Babysitter


class BabysitterAdminCreateForm(forms.ModelForm):
    # The only mention of this field is OK to make him Mandatory
    # In this way, the admin have to assure that the babysitter doesn't have any criminal records
    criminal_record_attribute = forms.BooleanField(label="Casier Judiciaire (B1/B2) vierge", )

    class Meta:
        model = Babysitter
        # We are looking for every fields of the model
        fields = '__all__'

    def save(self, commit=True):
        babysitter = super(BabysitterAdminCreateForm, self).save(commit=False)
        # We don't forget to activate the criminal_record variable
        # It means that the babysitter doesn't have any criminal records
        babysitter.criminal_record = True
        if commit:
            babysitter.save()
        return babysitter


class BabysitterAdminChangeForm(forms.ModelForm):

    class Meta:
        model = Babysitter
        exclude = ['member', 'criminal_record', ]

