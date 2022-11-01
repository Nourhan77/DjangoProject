from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models
import re

# Create your models here.




class User(models.Model):
    First_name= models.CharField(max_length=25)
    Last_name= models.CharField(max_length=25)
    Email= models.EmailField(max_length=500)
    password= models.CharField(max_length=15)
    confirm_password= models.CharField(max_length=15)
    mobile_phone=models.CharField(max_length=11)
    donations=models.IntegerField(default=0)
    birthdate=models.DateField(null=True)
    facebook=models.CharField(null=True,max_length=50)
    country=models.CharField(null=True,max_length=50)
    profile_image= models.ImageField(null=True,blank=True,upload_to='images/')


    def __str__ (self):
        return self.First_name


    @classmethod
    def get_all (cls):
        return cls.objects.all()

    @classmethod
    def get_user (cls,bid):
        return cls.objects.filter(id=bid)
    
    @classmethod
    def clean_mobile(self,mobile):
        if  re.fullmatch("01[0125][0-9]{8}",mobile):
            return mobile
        else: 
            mobile=""
        return mobile


    