from .base_owners_test import BaseOwnersTest

import string

import pdb

class OwnersRedirectTest(BaseOwnersTest):



    def test_post_sql_injection_name(self):
    
        self.data["name"] = 'OR 1=1' 
        response = self.post(self.data)
                      
        self.assertEqual(response.status_code, 400)
        
    def test_post_sql_injection_link(self):
    
        self.data["link"] = 'OR 1=1' 
        response = self.post(self.data)
        
        self.assertEqual(response.status_code, 400)
  
    def test_post_name_validation(self):
        
        self.data["name"] = ' akqkmw e9z01 @ !!'
        
        response = self.post(self.data)
        
        self.assertEqual(response.status_code, 400)
        
    def test_post_link_validation(self):
        self.data['link'] = 'hkdw  qiqma 103 z ++(@@ '
        
        response = self.post(self.data)
        
        self.assertEqual(response.status_code, 400)
        
    def test_post_if_accepted_it_does_not_accept_a_name_with_more_than_32_characters(self):
        
        self.data['name'] = 'a'*33
        
        response = self.post(self.data)
        
        self.assertEqual(response.status_code, 400)
        
    def test_post_if_accepted_it_does_not_accept_a_link_with_more_than_256_characters(self):
        
        self.data['link'] = f'https://{"a" * 300}.com'
        
        response = self.post(self.data)
        
        self.assertEqual(response.status_code, 400)
    
    def test_post_shortened_url(self):    
        
        response = self.post(self.data)
                        
        self.assertEqual(response.status_code, 201)        
                                     
    def test_post_shorten_the_same_url(self):
    
        data = {
        
            'name': 'teste-link-other',
            'link': 'https://test.com'
        
        }
         
        self.post(self.data)
        
        response = self.post(data)
        
        self.assertEqual(response.status_code, 400)
            
    def test_post_if_it_is_not_possible_to_shorten_the_same_name(self):
    
        data = {
        
          'name': 'test-name',
          'link': 'https://othertest.com'
        }            
        
        self.post(self.data)
        response = self.post(data)
        self.assertEqual(response.status_code, 400)        
                 
    def test_post_if_user_can_short_more_than_10_urls(self):
        responses = []

        characters = string.ascii_letters
        
        for i in range(14):
            name =  'teste-name' + str(i)
            data = {
                'name': name,
                'link': f'https://{name}.com'
            }
            
            response = self.post(data)
            responses.append(response.status_code)
                            
        for response in responses[:10]:
            self.assertEqual(response, 201)

        for response in responses[12:]:
            self.assertEqual(response, 400)