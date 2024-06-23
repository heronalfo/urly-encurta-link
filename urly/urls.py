from django.urls import path, include
from .swagger import swagger_view

urlpatterns = [

    path('swagger/', swagger_view.with_ui('swagger'), name='schema-swagger-ui'),  
    path('redoc/', swagger_view.with_ui('redoc'), name='schema-redoc'),
    path('links/', include('links.urls')), 
    path('tokens/', include('tokens.routers')),
    path('owners/', include('owners.routers')),
    
]
