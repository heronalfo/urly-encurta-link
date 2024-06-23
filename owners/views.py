from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle
from rest_framework_xml.renderers import XMLRenderer
from rest_framework_xml.parsers import XMLParser

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from .examples import responses
from .permissions import IsOwner
from links.serializers import RedirectsSerializer
from links.models import Redirects

class OwnerRedirectionViewSet(ModelViewSet):
    """
    ViewSet to manage URL redirects owned by authenticated users.
    Allows create, update, delete, and list operations.
    """
                
    queryset = Redirects.objects.all()
    serializer_class = RedirectsSerializer
    parser_classes = [JSONParser, XMLParser]
    renderer_classes = [JSONRenderer, XMLRenderer]
    http_method_names = ['options', 'head', 'get', 'post', 'delete', 'patch']
    
    def perform_create(self, serializer):
        """
        Sets the owner of the redirect to the authenticated user when creating a new redirect.
        """
        serializer.save(owner=self.request.user)
        super().perform_create(serializer)

    def get_object(self):
        """
        Retrieves the object to be manipulated, ensuring the user has permissions for it.
        """
        pk = self.kwargs.get('pk')
        obj = get_object_or_404(self.get_queryset(), pk=pk)
        self.check_object_permissions(self.request, obj)
        return obj

    def get_permissions(self):
        """
        Returns the permissions for the current action.
        """
        if self.action == 'create':
            return [IsAuthenticated()]
        if self.action in ['update', 'destroy', 'list']:
            return [IsOwner()]
        return super().get_permissions()
        
    @swagger_auto_schema(
        operation_description='List of URLs belonging to you',
        responses={200: responses}
    )
    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        return response
        
    @swagger_auto_schema(
        operation_description='Shortening new URLs. It is not possible to shorten more than 10 URLs',
        responses={
            201: 'Successfully shortened URL',
            400: 'Errors with designated parameters',
            401: 'It is not possible to shorten more than 10 URLs',
        }
    )
    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return response
    
    @swagger_auto_schema(
        operation_description='Editing shortenings. It is not possible to shorten to an existing URL',
        responses={
            200: 'URL edited successfully',
            400: 'Problems with standardizing or shortening an existing URL',
        },
    )
    def partial_update(self, request, *args, **kwargs):
        response = super().partial_update(request, *args, **kwargs)
        return response
        
    @swagger_auto_schema(
        operation_description='URL restructuring, exclude shortening. You can only delete your own URLs',
        responses={
            200: 'URL deleted successfully',
            400: 'Errors with designated parameters',
            401: 'This URL does not belong to you'
        },
    )
    def destroy(self, request, *args, **kwargs):
        response = super().destroy(request, *args, **kwargs)
        return response