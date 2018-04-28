from __future__ import unicode_literals
from django.db import models
from django.core.validators import RegexValidator

class PostModel(models.Model):
    username = models.CharField(validators=[RegexValidator(regex='^.{8}', message='Length has to be 8', code='nomatch')],max_length=150,blank=True)
    Email = models.EmailField(max_length=70)
    year = models.IntegerField(editable=True)
    statechoices =(('Delhi','DELHI'),('Mumbai','MUMBAI'),('Agra','AGRA'))
    states = models.CharField(choices=statechoices,max_length=10)
    image =models.FileField(upload_to='home/Downloads/')
    Remember_me = models.BooleanField(blank=True,default=True)
    accept_Terms_Conditions =models.BooleanField(blank=False,default=True)
    GENDER_CHOICES = (('M', 'Male'),('F', 'Female'))
    gender = models.CharField(choices=GENDER_CHOICES, max_length=56,default=None)
    Description = models.TextField(blank=True,null=True)

    def __str__(self):
        return self.username


class sort(models.Model):
    choices = (('usernameatoz','By username A-Z'),('usernameztoa','By username Z-A'),('emailatoz','By Email A-Z'),('emailztoa','By Email Z-A'))
    sortchoices = models.CharField(choices=choices,max_length=10,default=choices[0])
