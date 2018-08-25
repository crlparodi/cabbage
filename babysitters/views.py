from django.shortcuts import render
from django.http import Http404
from .models import Babysitter
from accounts.models import Member
from .search import SearchForm


def show_db_list(request):
    qs = Babysitter.objects.all().order_by('price_unit', 'price')
    return render(request, 'babysitters/list.html', {'qs': qs})


def search(request):
    form = SearchForm()
    return render(request, 'babysitters/search.html', {'form': form})


def results(request):
    try:
        forms = SearchForm(request.POST)
        qs = Babysitter.objects.filter(
            member__full_name__contains=forms['name'].data,
            # we are picking the 'full_name' attribute from the OneToOneField member
            age_target__contains=forms['age_target'].data,
            time_target__contains=forms['time_target'].data,
            location__contains=forms['location'].data
        )
    except ValueError:
        raise Http404("Oops ! La recherche semble avoir échoué. Veuillez réessayer.")

    return render(request, 'babysitters/results.html', {'qs': qs, 'forms': forms})
