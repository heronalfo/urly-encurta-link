from rest_framework import serializers
from rest_framework import status
from utils import (validate_link,  validate_slug)
import re
from .models import Redirects

class RedirectsSerializer(serializers.ModelSerializer):

    """
    
    Serializer intended for validating and transforming data for the Redirects model 
        
    """

    class Meta:
    
        model = Redirects
        fields = ['id', 'name', 'link', 'owner', 'date']
        read_only_fields = ['owner', 'date']
                
    def validate_name(self, name):
        
        if not validate_slug(name):
        
            raise serializers.ValidationError({'detail': 'The (name) does not match the standards; use as an example: exemple-slug'})
        
        if name and len(name) > 32:
        
            raise serializers.ValidationError({'detail': 'The (name) of URL must be less than 32 characters'})
        
        return name
    
    def validate_link(self, link):
    
        if not validate_link(link):
        
            raise serializers.ValidationError({'detail': 'Your URL does not match the standards; use as an example: https://<your-url>.host'})
                                   
        if len(link) > 255:
        
            raise serializers.ValidationError({'detail': 'The (link) of URL must be less than 255 characters'})
            
        return link
    
    def validate(self, attrs):
    
        _validate = super().validate(attrs)
    
        request = self.context.get('request')
                  
        owner_redirects = Redirects.objects.all().filter(owner=request.user)
        
        if Redirects.objects.all().filter(name=attrs.get('name')).exists():
        
            raise serializers.ValidationError({'detail': 'You have already shortened this name, it is not possible to shorten it again'})
                               
        if owner_redirects.count() > 10:
                   
            raise serializers.ValidationError({'detail': 'You have already shortened more than 10 URLs, you cannot shorten more'})
                                    
        if owner_redirects.filter(link=request.data.get('link')).exists():
            
            raise serializers.ValidationError({'detail': 'You have already shortened this URL, it is not possible to shorten it again'})
            
        return _validate