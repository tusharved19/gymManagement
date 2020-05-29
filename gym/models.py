from django.db import models

# Create your models here.

class Enquiry(models.Model):
    Name = models.CharField(max_length=20)
    Contact = models.CharField(max_length=10)
    EmailID = models.CharField(max_length=30)
    Age = models.CharField(max_length=20)
    Gender = models.CharField(max_length=6)

    def __str__(self):
        return self.name 

class Equipment(models.Model):
    name = models.CharField(max_length=50)
    price = models.CharField(max_length=10)
    unit = models.CharField(max_length=30)
    date = models.CharField(max_length=20)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name 

class Plan(models.Model):
    name = models.CharField(max_length=50)
    amount = models.CharField(max_length=10)
    duration = models.CharField(max_length=10)
    

    def __str__(self):
        return self.name 

class Member(models.Model):
    name = models.CharField(max_length=20)
    contact = models.CharField(max_length=10)
    emailid = models.CharField(max_length=30)
    age = models.CharField(max_length=2)
    gender = models.CharField(max_length=6)
    plan = models.CharField(max_length=30)
    joindate = models.CharField(max_length=10)
    expiredate = models.CharField(max_length=10)
    initialamount = models.CharField(max_length=10)

    def __str__(self):
        return self.name 