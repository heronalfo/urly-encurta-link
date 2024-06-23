from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import *

owners_simple_router = SimpleRouter()
owners_simple_router.register('api/v1', OwnerRedirectionViewSet, basename='owners')

urlpatterns = [

] + owners_simple_router.urls