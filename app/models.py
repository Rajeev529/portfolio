from django.db import models

# Create your models here.

class bioData(models.Model):
    role=models.CharField(max_length=20,default='none')
    key=models.BigIntegerField()
    name=models.CharField(max_length=20)
    dob=models.CharField(max_length=20)
    email=models.EmailField()
    linkdin=models.URLField()
    contact=models.CharField(max_length=15)
    gitlink=models.URLField(max_length=200)
    leetcodelink=models.URLField(max_length=200)
    istrue=models.BooleanField(default=False)
class exp(models.Model):
    role=models.CharField(max_length=20,default='none')
    key=models.BigIntegerField()
    title=models.CharField()
    desc=models.TextField()
    cred=models.URLField()
class project(models.Model):
    role=models.CharField(max_length=20,default='none')
    image=models.URLField()
    prjurl=models.URLField()
    title=models.CharField()

