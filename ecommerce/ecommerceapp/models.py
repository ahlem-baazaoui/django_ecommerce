
from django.db import models
from uuid import uuid4
# Create your models here.
class Member(models.Model):
 full_name = models.CharField(max_length=255)
 email = models.EmailField(unique = True)
 twitter = models.CharField(max_length=255, null=True, blank=True)
 linkedin = models.CharField(max_length=255, null=True, blank=True)
 facebook = models.CharField(max_length=255, null=True, blank=True)
 website = models.CharField(max_length=255, null=True, blank=True) 
 picture = models.FileField(null=True, blank=True)

def __str__(self):
  return self.full_name

def upload_picture(instance, filename):
  extension = filename.split('.')[-1]
  return 'static/uploads/Member/{}.{}'.format(uuid4().hex, extension)



class Members(models.Model):
  picture = models.FileField(upload_to=upload_picture, null= True)
