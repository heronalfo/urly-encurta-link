import re

def validate_link(link: str) -> bool:

    pattern = re.compile(r'^(?:https?|ftp):\/\/[-A-Za-z0-9+&@#\/%?=~_|!:,.;]*[-A-Za-z0-9+&@#\/%=~_|]')
      
        
    match = re.match(pattern, link)
        
    if match is None:
    
        return False
    
    return True
    
        
        
