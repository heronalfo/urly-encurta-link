from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

class Redirects(models.Model):

    """
    
     Table designed to store the data necessary for shortening URLS 
    
    """

    owner = models.ForeignKey(User, models.CASCADE, related_name='redirects')
       
    name = models.SlugField(max_length=32, unique=True, blank=False, null=False)
    
    link = models.CharField(max_length=255, blank=False, null=False)
    
    date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
    
        ordering = ['-date']
        app_label = 'links'
        verbose_name = 'Redirect'
        verbose_name_plural = 'Redirects'        
        
    class Index:
    
        fields = ['name', ]
     
    def __str__(self):
    
        return self.name
    
    def save(self, *args, **kwargs):
    
        """
        
         Transforms the name into a slug automatically so there is no interference  
        
        """
    
        self.name = slugify(self.name)        
        super().save(*args, **kwargs)
        
