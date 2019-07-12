from django.urls import path
from apps.navigation.views.views import *

urlpatterns = [
    path('', home, name='home'),
    path('search/', search),
    path('results/', results),
    path('profile/<int:id>$', display_babysitter, name='babysitter_profile')
]
