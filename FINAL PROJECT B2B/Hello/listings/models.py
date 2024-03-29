from django.db import models
from datetime import datetime
from core.models import User

class Listing(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    category=models.CharField(max_length=100)
    address=models.TextField()
    city=models.CharField(max_length=100)
    pincode=models.CharField(max_length=100)

    state=models.CharField(max_length=100)
    price=models.IntegerField()
    description=models.TextField(blank=True)
    photo_main=models.ImageField(upload_to='photos/%Y/%m/%d')
    photo_1=models.ImageField(upload_to='photos/%Y/%m/%d',blank=True)
    photo_2=models.ImageField(upload_to='photos/%Y/%m/%d',blank=True)
    photo_3=models.ImageField(upload_to='photos/%Y/%m/%d',blank=True)
    photo_4=models.ImageField(upload_to='photos/%Y/%m/%d',blank=True)
    photo_5=models.ImageField(upload_to='photos/%Y/%m/%d',blank=True)
    photo_6=models.ImageField(upload_to='photos/%Y/%m/%d',blank=True)
    is_published=models.BooleanField(default=True)
    list_date=models.DateField(default=datetime.now)

    def __str__(self):
        return self.title

    
    
    

    



# Create your models here.
