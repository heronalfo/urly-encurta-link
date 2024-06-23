from .base_owners_test import BaseOwnersTest

class TestOwnersHTTPMethodNames(BaseOwnersTest):

    def test_it_allowed_method_patch(self):
    
        response = self.client.patch(self.api_url)
        
        self.assertEqual(response.status_code, 405)
        
        