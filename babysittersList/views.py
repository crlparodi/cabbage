from django.shortcuts import render
from django.db.models.functions import Lower
from .models import Babysitter


# Create your views here.
def list(request):
    babysitters = Babysitter.objects.all().order_by('price_unit', 'price')
    return render(request, 'babysittersList/list.html', {'babysitters': babysitters})

def search(request):
    return render(request, 'babysittersList/search.html', {})