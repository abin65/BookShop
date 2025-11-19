from django.db import models

# Create your models here.
class categorydb(models.Model):
    cat_name = models.CharField(max_length=100,null=True,blank=True)
    cat_description = models.CharField(max_length=100,null=True,blank=True)
    cat_cover_image = models.ImageField(upload_to="cover image",null=True,blank=True)
    def __str__(self):
        return self.cat_name

class bookdb(models.Model):
    book_title = models.CharField(max_length=100,null=True,blank=True)
    book_author = models.CharField(max_length=100,null=True,blank=True)
    book_category = models.CharField(max_length=100,null=True,blank=True)
    book_price = models.IntegerField(null=True,blank=True)
    book_publisher = models.CharField(max_length=100,null=True,blank=True)
    book_description = models.CharField(max_length=100,null=True,blank=True)
    book_cover_image = models.ImageField(upload_to="cover image",null=True,blank=True)
    def __str__(self):
        return self.book_title
