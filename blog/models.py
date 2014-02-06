from django.db import models

class Post(models.Model):
    title = models.CharField(max_length = 200)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add = True)

    def __unicode__(self):
        return self.title
    
    def is_small(self):
        return len(self.body) <= 50

# Create your models here.
