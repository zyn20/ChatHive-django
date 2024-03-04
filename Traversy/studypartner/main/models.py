from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Topic(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name
    
class Room (models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL,null=True) 
    # defining the relationship like one room has only one topic but a topic can have multiple rooms 
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL,null=True)
    name = models.CharField(max_length=200)
    description = models.TextField(null = True,blank=True)
    # participants =
    updated = models.DateTimeField(auto_now = True) 
    #auto_now update the instance when we save instance every time or take timestamp every single time
    created = models.DateTimeField(auto_now_add = True)
    # auto_now_add takes the time when first time instance was created or inital timestamp
    
    class Meta:
        ordering = ['-updated','-created']
    
    def __str__(self):
        return self.name
class Message (models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    room = models.ForeignKey(Room,on_delete=models.CASCADE)
    # on _delete = models.CASCADE means if room is deleted then all of that messages will also be deleted representing one to many relationship
    body = models.TextField()
    updated = models.DateTimeField(auto_now = True) 
    created = models.DateTimeField(auto_now_add = True)
    def __str__(self):
        return self.body[0:50]
    
     
    
     