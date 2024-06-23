from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework.permissions import IsAuthenticated 

from rest_framework.throttling import AnonRateThrottle

from rest_framework_xml.renderers import XMLRenderer
from rest_framework_xml.parsers import XMLParser

from .serializers import CreateUserSerializer

from .permissions import IsOwnerOfUser

class AuthenticationCreateUser(ModelViewSet):

    queryset = User.objects.all()

    serializer_class = CreateUserSerializer
    
    parser_classes = [JSONParser,  XMLParser]
    
    renderer_classes = [JSONRenderer, XMLRenderer]
    
    throttle_classes = [AnonRateThrottle]
       
    http_method_names = ['post', 'patch', 'delete', 'head', 'options']
       
    def perform_create(self, serializer):
    
        user = serializer.data
    
        User.objects.create_user(
                
            username = user['username'],
            
            password = user['password']
            
        )
        
    def get_object(self):
    
        user = self.request.user.username
        
        obj = get_object_or_404(
        
            self.get_queryset(),
            pk=self.request.user
        
        )        
      
        
        self.check_object_permissions(self.request, obj)
        
        return obj
    
    def get_permissions(self):
    
        if self.action in ['destroy', 'update']:
        
            return [IsAuthenticated(), IsOwnerOfUser()]
            
        return super().get_permissions()
    
              
    
    
    