from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework import status
from utils import validate_slug

class CreateUserSerializer(serializers.ModelSerializer):

    class Meta:
    
        model = User
        fields = [ 'username', 'password' ]
    
    def validate(self, attrs):
    
        _validate = super().validate(attrs)
        
        if not validate_slug(attrs.get('username')):
        
            raise serializers.ValidationError({'detail': 'The NAME does not match the standards; use as an example: exemple-slug'})
        
        if User.objects.all().filter(username=attrs.get('username')).exists():
        
            raise serializers.ValidationError({'detail': 'The username already exists'})
        
        if len(attrs.get('password')) < 8:
        
            raise serializers.ValidationError({'detail': 'The PASSWORD must have 8 or more chadacters'})
                       
        return _validate