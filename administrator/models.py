from django.db import models

# Create your models here.

class LoginTable(models.Model):
    username = models.CharField(max_length=30,null=True,blank=True)
    password=models.CharField(max_length=30,null=True,blank=True)
    usertype=models.CharField(max_length=30,null=True,blank=True)
    

class User(models.Model):
    name=models.CharField(max_length=30,null=True,blank=True)
    email=models.CharField(max_length=30,null=True,blank=True)
    gender=models.CharField(max_length=30,null=True,blank=True)
    phoneno=models.IntegerField(null=True,blank=True)
    DOB=models.CharField(max_length=30,null=True,blank=True)
    place=models.CharField(max_length=30,null=True,blank=True)
    post=models.CharField(max_length=30,null=True,blank=True)
    pin=models.IntegerField(null=True,blank=True)
    LOGIN_ID=models.ForeignKey(LoginTable, on_delete=models.CASCADE,null=True,blank=True)

    
class clubtable(models.Model):
    LOGIN_ID=models.ForeignKey(LoginTable, on_delete=models.CASCADE,null=True,blank=True)
    name=models.CharField(max_length=30,null=True,blank=True)
    place=models.CharField(max_length=30,null=True,blank=True)
    post=models.CharField(max_length=30,null=True,blank=True)
    pin=models.IntegerField(null=True,blank=True)
    phoneno=models.IntegerField(null=True,blank=True)
    email=models.CharField(max_length=30,null=True,blank=True)

class activities(models.Model):
    item=models.CharField(max_length=30,null=True,blank=True)
    rules=models.CharField(max_length=30,null=True,blank=True)
    description=models.CharField(max_length=30,null=True,blank=True)
    status=models.CharField(max_length=30,null=True,blank=True)
    level=models.CharField(max_length=30,null=True,blank=True)
    CLUB=models.ForeignKey(clubtable, on_delete=models.CASCADE,null=True,blank=True)
    
class complaints(models.Model):
    complaints=models.CharField(max_length=60,null=True,blank=True)
    created_at=models.DateField(auto_now_add=True)
    updated_at=models.DateField(auto_now=True)
    reply=models.CharField(max_length=60,null=True,blank=True)
    USER=models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)

    
class notification(models.Model):
    notification=models.CharField(max_length=60,null=True,blank=True)
    date=models.CharField(max_length=20,null=True,blank=True)
    time=models.CharField(max_length=60,null=True,blank=True)
    reply=models.CharField(max_length=60,null=True,blank=True)


    
class notificationtable(models.Model):
    notification=models.CharField(max_length=60,null=True,blank=True)
    date=models.CharField(max_length=20,null=True,blank=True)
    

class servicetable(models.Model):
    services=models.CharField(max_length=60,null=True,blank=True)
    description=models.CharField(max_length=400,null=True,blank=True)
    CLUB=models.ForeignKey(clubtable, on_delete=models.CASCADE,null=True,blank=True)
    status=models.CharField(max_length=100,null=True,blank=True)

class event(models.Model):
    eventname= models.CharField(max_length=60,null=True,blank=True)
    date=models.CharField(max_length=60,null=True,blank=True)
    description=models.CharField(max_length=400,null=True,blank=True)
    CLUB=models.ForeignKey(clubtable,on_delete=models.CASCADE,null=True,blank=True)

class feedback(models.Model):
    feedback=models.CharField(max_length=60,null=True,blank=True)
    created_at=models.DateField(auto_now_add=True,null=True,blank=True)
    updated_at = models.DateField(auto_now=True)
    USER=models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)



class instructions(models.Model):
    instructions=models.CharField(max_length=60,null=True,blank=True)
    date=models.CharField(max_length=60,null=True,blank=True)

class ratingclass(models.Model):
    rating=models.CharField(max_length=60,null=True,blank=True)
    description=models.CharField(max_length=400,null=True,blank=True)

class addandmanagemembers(models.Model):
     name=models.CharField(max_length=30,null=True,blank=True)
     Department=models.CharField(max_length=30,null=True,blank=True)
     year=models.CharField(max_length=30,null=True,blank=True)
     club=models.CharField(max_length=30,null=True,blank=True)
     email=models.CharField(max_length=30,null=True,blank=True)
     phoneno=models.IntegerField(null=True,blank=True)
     status=models.CharField(max_length=100,null=True,blank=True)

class register(models.Model):
    fullname=models.CharField(max_length=100,null=True,blank=True)
    username=models.CharField(max_length=100,null=True,blank=True)
    email=models.CharField(max_length=30,null=True,blank=True)
    password=models.CharField(max_length=30,null=True,blank=True)
    phoneno=models.IntegerField(null=True,blank=True)
    gender=models.CharField(max_length=30,null=True,blank=True)

class request(models.Model):
      USER=models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
      club_id=models.CharField(max_length=30,null=True,blank=True)
      status=models.CharField(max_length=30,null=True,blank=True)

class clubLogin(models.Model):
    username = models.CharField(max_length=30,null=True,blank=True)
    password=models.CharField(max_length=30,null=True,blank=True)
    usertype=models.CharField(max_length=30,null=True,blank=True)
    






   





