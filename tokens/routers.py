from django.urls import path
from rest_framework.routers import SimpleRouter

from rest_framework_simplejwt.views import (

    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from .viewsets import AuthenticationCreateUser

app_name = "tokens"

routers = SimpleRouter()

routers.register('api/v1', AuthenticationCreateUser, basename='tokens')

urlpatterns = [

    path('api/token/', TokenObtainPairView.as_view(), name='token'),
    
    path('api/token/refresh/', TokenRefreshView.as_view(), name='refresh'),
    
    path('api/token/verify/', TokenVerifyView.as_view(), name='verify'),
        
] + routers.urls