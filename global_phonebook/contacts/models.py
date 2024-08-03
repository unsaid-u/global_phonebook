from django.db import models

# Create your models here.

class Contacts(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    phone_no = models.CharField(max_length=20, db_index=True)  
    code= models.CharField(max_length=10)
    is_spam = models.BooleanField(default=False)
    is_registered = models.BooleanField(default=False)
    user_id = models.IntegerField(null=True, blank=True) 
    email = models.EmailField(unique=False, null=True, blank=True)