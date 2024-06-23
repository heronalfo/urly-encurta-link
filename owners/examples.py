from drf_yasg import openapi

responses = openapi.Response(

    'URL found',
    
    examples = {'application/json': [
      
      
        {
        
            'id': 1,
            'owner': 1,
            'name': 'urly',
            'link': 'https://urly.net'
        
        },
        
        {
        
        
            'id': 2,
            'owner': 1,
            'name': 'url-name',
            'link': 'https://example.com'
        
           
            
        
        },                                                                                                                                                                                                                                 
         
     ],
    
   }

)