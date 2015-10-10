from django.db import models
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.core.urlresolvers import reverse

from dbe.blog.models import *

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=60)
    body=models.TextField()
    created=models.DateTimeField(auto_now_add=True)
    
    def _unicode_(self):
        returnself.title
        
class PostAdmin(admin.ModelAdmin):
     search_fields= ["title"]
    
admin.site.register(Post,PostAdmin)

def main(request)