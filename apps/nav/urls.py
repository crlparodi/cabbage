from django.urls import path, re_path
from apps.nav.views.views import *

urlpatterns = [
    path('', home, name='home'),
    path('search/', search),
    path('results/', results),
    path('profile/<int:id>', display_babysitter, name='babysitter_profile')

]
