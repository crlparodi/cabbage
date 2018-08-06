from django.shortcuts import render
from django.db.models.functions import Lower
from .models import *


# Create your views here.
def home(request):
    return render(request, 'babysittersList/home.html', {})

def list(request):
    babysitters = Babysitter.objects.all().order_by('price_unit', 'price')
    return render(request, 'babysittersList/list.html', {'babysitters': babysitters})

def search(request):
    forms = SearchForm()
    return render(request, 'babysittersList/search.html', {'forms': forms})

def results(request):
    query = str(request.POST.get('bar'))
    if query.__len__() < 2:
        results = None
    else:
        results = Babysitter.objects.filter(name__contains=query)
    return render(request, 'babysittersList/results.html', {"results": results, "query": query, })

