from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken
from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
import string

class BaseOwnersTest(TestCase):

    def setUp(self):
        self.client = APIClient()
    
        self.user = User.objects.create_user(username='client-test', password='Abc123')
        
        self.client.force_authenticate(user=self.user)
        
        refresh = RefreshToken.for_user(user=self.user)
        
        self.token = str(refresh.access_token)
        
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')
        
        self.data = {
            'name': 'test-name',
            'link': 'https://test.com'
        }
        
        self.data_xml = f'''
        
        <root>
        
            
            
            {self.data["name"]}
            
            
            
            
            {self.data["link"]}
                
            
        </root>
        
        '''
        
        self.api_url = reverse('owners-list')

    def post(self, data=None):
    
        return self.client.post(self.api_url, data, format='json')
        
    def patch(self, data=None):
    
        create = self.post(self.data).data
                        
        api_url = reverse('owners-detail', kwargs={'pk': create['id']})
        
        return self.client.patch(api_url, data, format='json')