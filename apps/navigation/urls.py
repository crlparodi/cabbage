from django.urls import include, path
from apps.navigation.views.views import *
from apps.authentication.views.views import *

urlpatterns = [
    path('', home, name='home'),
    # apps.navigation.views.views.search
    path('search/', search),
    # apps.navigation.views.views.results
    path('results/', results),
    # User Profile
    path('profile/<int:pk>', CabbageUserProfileUpdate.as_view(),
         name='member_details'),
    path('profile/<int:pk>/babysitter',
         CabbageBabysitterProfileUpdate.as_view(), name='babysitter_details'),
]
