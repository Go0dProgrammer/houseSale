from django.db import models
from django.contrib.auth.models import User
import datetime

from django.db.models.deletion import CASCADE

#Models become a db tables thanks to django.

class Ad(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    img = models.ImageField(upload_to='static/img/ad/%Y.%m.%d')
    price = models.IntegerField()
    houseArea = models.IntegerField()
    territoryArea = models.IntegerField()
    city = models.CharField(max_length=50)
    street = models.CharField(max_length=50)
    house = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now=True)

    #Return undertsble title to admin panel.
    def __str__(self):
        return self.title
    
