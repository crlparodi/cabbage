
from django.urls import include, path
from apps.auth.views.api import *
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

router = DefaultRouter()
router.register(r'members', MemberViewSet, basename='member')
router.register(r'babysitters', BabysitterViewSet, basename='babysitter')

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls')),
    path('auth/token/', views.obtain_auth_token)
]
