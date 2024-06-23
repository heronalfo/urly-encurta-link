from django.db.models import Q
from django.utils import timezone

from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import pagination

from datetime import datetime, timedelta

from .models import Redirects
from .serializers import RedirectsSerializer

class StandardResultSetPagination(pagination.PageNumberPagination):

    page_size = 1000
    page_size_query_param = 'page'
    max_page_size = 10000

class LinksRedirect(ListAPIView):

    lookup_url_kwarg = 'name'
    
    queryset = Redirects.objects.all()

    serializer_class = RedirectsSerializer
    
    def get_queryset(self, *args, **kwargs):
    
        lookup_url_kwarg = self.kwargs.get('name')
        
        qs = super().get_queryset(*args, **kwargs).get(name=lookup_url_kwarg)
        
        return qs

class LinksSearch(LinksRedirect):

    def get_queryset(self, *args):
                    
        name = self.request.query_params.get('q')
        
        qs = super().get_queryset(*args).filter(name=name)
        
        return qs

class DataRedirect(APIView):

    def get(self, request):
    
        queryset = Redirects.objects.all()
    
        now = timezone.now()
        
        week = now - timedelta(days=7)
        
        month = now - timedelta(days=30)
                
        data = {
        
          "shortened_urls": queryset.count(),
                              
          "last_week": queryset.filter(date__gte=week, date__lte=now).count(),
          
          "last_month": queryset.filter(date__gte=month, date__lte=now).count()
        
        
        }                
        
        return Response(data)
        
        
        
        
        