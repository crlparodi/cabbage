from django.shortcuts import render
from apps.authentication.babysitters.models import Babysitter


def show_db_list(request):
    qs = Babysitter.objects.all().order_by('price_unit', 'price')
    return render(request, 'authentication/list.html', {'qs': qs})
