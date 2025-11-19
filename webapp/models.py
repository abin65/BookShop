from django.db import models

# Create your models here.
class registrationdb(models.Model):
    reg_user_name = models.CharField(max_length=100,null=True,blank=True)
    reg_password = models.CharField(max_length=100,null=True,blank=True)
    reg_conform_password = models.CharField(max_length=100,null=True,blank=True)
    reg_email = models.EmailField(max_length=100,null=True,blank=True)

class contactdb(models.Model):
    contact_name = models.CharField(max_length=100,null=True,blank=True)
    contact_email = models.CharField(max_length=100,null=True,blank=True)
    contact_subject = models.CharField(max_length=100,null=True,blank=True)
    contact_message = models.CharField(max_length=100,null=True,blank=True)

class cartdb(models.Model):
    username = models.CharField(max_length=100,null=True,blank=True)
    bookname = models.CharField(max_length=100,null=True,blank=True)
    quantity = models.IntegerField(null=True,blank=True)
    price = models.IntegerField(null=True,blank=True)
    totalprice = models.IntegerField(null=True,blank=True)
    component_image = models.ImageField(upload_to="cart image",null=True,blank=True)


