"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from apps.authentication.views.views import *
from apps.navigation.views.views import *

urlpatterns = [
    path('admin/', admin.site.urls),        # django.contrib.admin.site.urls
    path('', home),                         # apps.navigation.views.views.home
    path('list/', show_db_list),            # apps.authentication.views.views.show_db_list
    path('search/', search),                # apps.navigation.views.views.search
    path('results/', results),              # apps.navigation.views.views.results
]
