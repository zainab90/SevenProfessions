from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class SlidShow (models.Model):
    slid_image = models.ImageField(upload_to='slide_show/', verbose_name="slide_show Photo", null=True)
    slid_title = models.TextField(null=True, verbose_name='slide_show title')

    def __str__(self):
        return f'{self.slid_title}'

    class Meta:
        verbose_name = 'SlidShow'
        verbose_name_plural = 'SlidShows'


class Category (models.Model):
    cat_name= models.CharField(max_length=250,verbose_name='Category Name')
    cat_image=models.ImageField(upload_to='Category_images/', verbose_name="Category Photo",null=True)
    cat_details=models.TextField(null=True, verbose_name='Category Detail')

    def __str__(self):
        return f'{self.cat_name}'
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

class Service (models.Model):
    serv_name = models.CharField(max_length=250, verbose_name='Service Name')
    serv_details=models.TextField(verbose_name='Service Detail')
    serv_Img = models.ImageField(upload_to='Service_images/',verbose_name='Service Photo', null=True)
    date = models.DateTimeField(auto_now=True,null=True,verbose_name='Date')
    # user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='x', blank=True)
    serv_cat=models.ForeignKey(Category,on_delete=models.CASCADE, related_name='y', verbose_name='Service Category')

    def __str__(self):
        return f'{self.serv_name}'


    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'


