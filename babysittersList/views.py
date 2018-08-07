from django.shortcuts import render
from django.http import Http404
from django.db.models.functions import Lower
from .models import *


# Create your views here.
def home(request):
    return render(request, 'babysittersList/home.html', {})

def list(request):
    babysitters = Babysitter.objects.all().order_by('price_unit', 'price')
    return render(request, 'babysittersList/list.html', {'babysitters': babysitters})

def search(request):
    form = SearchForm()
    return render(request, 'babysittersList/search.html', {'form': form})

def results(request):
    try:
        forms = SearchForm(request.POST)
        results = Babysitter.objects.filter(
            name__contains=forms['name'].data,
            age_target__contains=forms['age_target'].data,
            time_target__contains=forms['time_target'].data,
            location__contains=forms['location'].data,
        )
    except ValueError:
        raise Http404("Oops ! "
                      "La recherche semble avoir échoué pour des raisons techniques. "
                      "Veuillez réessayer.")


    return render(request, 'babysittersList/results.html', {"results": results, "name": forms['name'].data})


