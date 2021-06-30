from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=150)
    desc = models.TextField()



class ValueOfSpliteData(models.Model):
    rvolt = models.IntegerField(default=0)
    yvolt = models.IntegerField(default=0)
    bvolt = models.IntegerField(default=0)
    rcurrent = models.FloatField(max_length=9,default=0)
    ycurrent = models.FloatField(max_length=9,default=0)
    bcurrent = models.FloatField(max_length=9,default=0)
    battery = models.IntegerField(default=0)
    rybeuser = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_ryb', null=True)
    
    
    

class OnoffValue(models.Model):
    ronoff = models.IntegerField()
    yonoff = models.IntegerField()
    bonoff = models.IntegerField()


class AddDevice(models.Model):
    id = models.IntegerField( primary_key= True)
    name = models.CharField(max_length=100)
    adress = models.CharField(max_length=250)
    rmax = models.IntegerField()
    rmin = models.IntegerField()
    ymax = models.IntegerField()
    ymin = models.IntegerField()
    bmax = models.IntegerField()
    bmin = models.IntegerField()
    deviceuser = models.ForeignKey(User, on_delete=models.CASCADE, related_name='usersplit_devices', null=True)
    devicerybdata = models.OneToOneField(ValueOfSpliteData, on_delete=models.CASCADE, null=True)
