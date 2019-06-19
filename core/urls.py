"""core URL Configuration
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, nurse_name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), nurse_name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import include, path
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.admin.views.decorators import staff_member_required
from apps.navigation.views.views import *
from apps.authentication.views.views import *

urlpatterns = [
    # ADMIN
    # django.contrib.admin.site.urls
    path('admin/', admin.site.urls),
    # HOME
    # apps.navigation.views.views.home
    path('', home, name='home'),
    # AUTHENTICATION
    # path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/login/check/',
         cabbage_login_check,
         name='cabbage_login_check'),
    path('accounts/login/',
         CabbageLoginView.as_view(),
         name='login'),
    path('accounts/logout/',
         CabbageLogoutView.as_view(),
         name='logout'),
    path('accounts/password_change/',
         CabbagePasswordChangeView.as_view(),
         name='password_change'),
    path('accounts/password_change/done/',
         CabbagePasswordChangeDone.as_view(),
         name='password_change_done'),
    path('accounts/password_reset/',
         CabbagePasswordResetView.as_view(),
         name='password_reset'),
    path('accounts/password_reset/done/',
         CabbagePasswordResetDone.as_view(),
         name='password_reset_done'),
    path('accounts/reset/<uidb64>/<token>/',
         CabbagePasswordResetConfirm.as_view(),
         name='password_reset_confirm'),
    path('accounts/reset/done/',
         CabbagePasswordResetComplete.as_view(),
         name='password_reset_complete'),
    # NAVIGATION
    # apps.navigation.views.views.search
    path('search/', search),
    # apps.navigation.views.views.results
    path('results/', results),
]
