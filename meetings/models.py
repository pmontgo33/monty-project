#   meetings/models.py
#   Models for the Meetings App
#   Patrick W. Montgomery
#   created: 9/19/2016

#   import statements
from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField

#   minutes model
class Minutes(models.Model):
    
    #   Minutes properties
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    meeting_date = models.DateTimeField(default=timezone.now)
    distribution = models.TextField()
    body = RichTextField()
    
    #   string representation function
    def __str__(self):
        return self.title
    