from ast import Try
from django.db import models

from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.urls import reverse
from django.db.models.fields import BigAutoField
import books

class admindetails(models.Model):
    user_id = BigAutoField(primary_key=True)
    username = models.CharField(max_length=60,null = True,blank = True,default=None)
    signup_otp = models.CharField(max_length=4)
    emailId = models.EmailField()
    password = models.CharField(max_length=8 ,unique=True , blank=False, error_messages={'required': 'Password cannot be null'})

    def __str__(self):
        return str(self.user_id) 

class studentdetails(models.Model):
    user_id = BigAutoField(primary_key=True)
    username = models.CharField(max_length=60,null = True,blank = True,default=None)
    signup_otp = models.CharField(max_length=4)
    emailId=models.EmailField()
    password = models.CharField(max_length=8 ,unique=True , blank=False, error_messages={'required': 'Password cannot be null'})

    def __str__(self):
        return str(self.user_id) 

class Books(models.Model):
    book_id = BigAutoField(primary_key=True)
    title = models.CharField(max_length=60,null = True,blank = True,default=None)
    Author = models.CharField(max_length=60,null = True,blank = True,default=None)
    issued_to = models.CharField(max_length=60,null = True,blank = True,default=None)
    issued_at = models.DateTimeField(auto_now=True)
    issued_status=models.BooleanField(null = True,blank = True,default=False)

    
def __str__(self):
        return str(self.book_id) 