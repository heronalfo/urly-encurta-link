from datetime import timedelta
from .security import SECRET_KEY

SIMPLE_JWT = {

 "ACCESS_TOKEN_LIFETIME": timedelta(days=30), 
 
 "REFRESH_TOKEN_LIFETIME": timedelta(days=60), 
 
 "ROTATE_REFRESH_TOKENS": False, 
 
 "BLACKLIST_AFTER_ROTATION": False,
  
 "SIGNING_KEY": SECRET_KEY,
    
 "AUTH_HEADER_TYPES": ("Bearer",), 
  
}