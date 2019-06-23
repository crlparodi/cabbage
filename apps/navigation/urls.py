from django.urls import include, path
from apps.navigation.views.views import *
from apps.authentication.views.views import *

urlpatterns = [
    path('', home, name='home'),
    # apps.navigation.views.views.search
    path('search/', search),
    # apps.navigation.views.views.results
    path('results/', results),
]
