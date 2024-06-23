import re

def validate_slug(slug: str) -> bool:

    pattern = re.compile('^[a-z0-9]+(?:-[a-z0-9]+)*$')
        
    if re.match(pattern, slug) is None:
    
        return False
   
    else: 
    
        return True
    
        