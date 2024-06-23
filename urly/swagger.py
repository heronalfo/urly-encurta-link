from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

swagger_view = get_schema_view(

    openapi.Info(
    
        title = 'Urly APi',
        default_version = 'v1',
        description = 'Documentation and guidance for using our API, by Urly',
        
        contact = openapi.Contact('j040p3dr0s1lv4s4nt0s@gmail.com'),
        
        license = openapi.License(name='Urly License'),
                        
    ),
            
    public = True,
    
    permission_classes = (permissions.AllowAny, ),
                
)