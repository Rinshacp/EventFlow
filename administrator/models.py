from django.db import models

# Create your models here.

class LoginTable(models.Model):
    username = models.CharField(max_length=30,null=True,blank=True)
    password=models.CharField(max_length=30,null=True,blank=True)
    usertype=models.CharField(max_length=30,null=True,blank=True)
    status=models.CharField(max_length=30,null=True,blank=True)
    

class User(models.Model):
    LOGIN_ID=models.ForeignKey(LoginTable, on_delete=models.CASCADE,null=True,blank=True)
    name=models.CharField(max_length=30,null=True,blank=True)
    email=models.CharField(max_length=30,null=True,blank=True)
    gender=models.CharField(max_length=30,null=True,blank=True)
    phoneno=models.IntegerField(null=True,blank=True)
    DOB=models.CharField(max_length=30,null=True,blank=True)
    place=models.CharField(max_length=30,null=True,blank=True)
    post=models.CharField(max_length=30,null=True,blank=True)
    pin=models.IntegerField(null=True,blank=True)

class clubcoordinator(models.Model):
    LOGIN_ID = models.ForeignKey(LoginTable, on_delete=models.CASCADE, null=True, blank=True)
    name=models.CharField(max_length=30,null=True,blank=True)
    email=models.CharField(max_length=30,null=True,blank=True)
    gender=models.CharField(max_length=30,null=True,blank=True)
    phoneno=models.IntegerField(null=True,blank=True)
    DOB=models.CharField(max_length=30,null=True,blank=True)
    place=models.CharField(max_length=30,null=True,blank=True)
    post=models.CharField(max_length=30,null=True,blank=True)
    pin=models.IntegerField(null=True,blank=True)




    
class event(models.Model):
    LOGIN_ID=models.ForeignKey(LoginTable, on_delete=models.CASCADE,null=True,blank=True)
    eventname=models.CharField(max_length=30,null=True,blank=True)
    place=models.CharField(max_length=30,null=True,blank=True)
    post=models.CharField(max_length=30,null=True,blank=True)
    pin=models.IntegerField(null=True,blank=True)
    phoneno=models.IntegerField(null=True,blank=True)
    email=models.CharField(max_length=30,null=True,blank=True)
    status=models.CharField(max_length=30,null=True,blank=True)

class complaints(models.Model):
    USER=models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    complaints=models.CharField(max_length=60,null=True,blank=True)
    created_at=models.DateField(auto_now_add=True,null=True,blank=True)
    updated_at=models.DateField(auto_now=True,null=True,blank=True)
    reply=models.CharField(max_length=60,null=True,blank=True)


class notification(models.Model):
    notification=models.CharField(max_length=60,null=True,blank=True)
    date=models.CharField(max_length=20,null=True,blank=True)
    time=models.CharField(max_length=60,null=True,blank=True)
    reply=models.CharField(max_length=60,null=True,blank=True)


class feedback(models.Model):
    feedback=models.CharField(max_length=60,null=True,blank=True)
    created_at=models.DateField(auto_now_add=True,null=True,blank=True)
    updated_at = models.DateField(auto_now=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)


class instructions(models.Model):
    instructions=models.CharField(max_length=60,null=True,blank=True)
    date=models.CharField(max_length=60,null=True,blank=True)


class eventgallery(models.Model):
    eventID=models.ForeignKey(event, on_delete=models.CASCADE,null=True,blank=True)
    eventimage=models.FileField(upload_to='eventimage',null=True,blank=True)
    eventdate=models.DateTimeField(auto_now_add=True,null=True,blank=True)

class EventRequest(models.Model):
    eventID=models.ForeignKey(event, on_delete=models.CASCADE,null=True,blank=True)
    USER=models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    status=models.CharField(max_length=30,null=True,blank=True)