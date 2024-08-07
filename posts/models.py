from django.db import models

# Create your models here.

class Post (models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(null=True, blank=True)
    rate = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    
def _str_(self):
    return self.title

