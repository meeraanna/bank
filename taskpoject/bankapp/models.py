from django.db import models

account_type=(('a','Savings'),('b','Current'),('c','Fixed'),('d','Salary'))

class appform(models.Model):
    name=models.CharField(max_length=250)
    dob=models.DateField()
    age=models.IntegerField()
    address=models.TextField(max_length=250)
    email=models.EmailField()
    phoneno=models.IntegerField()
    gender=models.BooleanField()
    account=models.CharField(max_length=100,choices=account_type)
    material=models.CharField(default=True,max_length=50)
    district = models.CharField(max_length=250)
    branch = models.CharField(max_length=250)


