from django.urls import path
from .views import LinksRedirect, LinksSearch, DataRedirect

app_name = "links"

urlpatterns = [

  path('<str:name>/', LinksRedirect.as_view(), name='redirect'),
  
  path('api/v1/search/', LinksSearch.as_view(), name='search'),
  
  path('api/v1/dashboard/', DataRedirect.as_view(), name='dashboard'),
  
]