from django.shortcuts import render
from django.db.models.functions import Lower
from .models import Babysitter, User


# Create your views here.
def home(request):
    return render(request, 'babysittersList/home.html', {})

def list(request):
    babysitters = Babysitter.objects.all().order_by('price_unit', 'price')
    return render(request, 'babysittersList/list.html', {'babysitters': babysitters})

def search(request):
    return render(request, 'babysittersList/search.html', {})

def results(request):
    query = request.GET.get('bar')
    try:
        query = str(query)
    except ValueError:
        query = None
        results = None
    if query:
        results = Babysitter.objects.filter(name__contains=query)
    return render(request, 'babysittersList/results.html', {"results": results, "query": query, })

