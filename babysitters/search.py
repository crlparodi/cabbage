from django import forms
from babysitters import components


class SearchForm(forms.Form):
    name = forms.CharField(label="Nom, prénom", max_length=255, required=False)
    age_target = forms.ChoiceField(label="Tranche d'âge", choices=components.AGE_TARGET_EMPTY, required=False)
    time_target = forms.ChoiceField(label="Disponibilité", choices=components.TIME_TARGET_EMPTY, required=False)
    location = forms.ChoiceField(label="Ville", choices=components.LOCATIONS_EMPTY, required=False)
