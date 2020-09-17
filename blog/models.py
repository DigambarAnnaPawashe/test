from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=150)
    desc = models.TextField()



class ValueOfSpliteData(models.Model):
    id = models.IntegerField(primary_key= True)
    rvolt = models.IntegerField()
    yvolt = models.IntegerField()
    bvolt = models.IntegerField()
    rcurrent = models.FloatField(max_length=999)
    ycurrent = models.FloatField(max_length=999)
    bcurrent = models.FloatField(max_length=999)
    battery = models.IntegerField()

class OnoffValue(models.Model):
    ronoff = models.IntegerField()
    yonoff = models.IntegerField()
    bonoff = models.IntegerField()
