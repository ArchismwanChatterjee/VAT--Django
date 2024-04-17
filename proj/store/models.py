from django.db import models

# Create your models here.
class user(models.Model):
    name=models.CharField(max_length=50) # CharField accepts any kind of data input
    email=models.EmailField()
    pwd=models.CharField(max_length=50)
    class Meta:
        db_table="user"

class Student(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phno = models.CharField(max_length=15)
    addr = models.CharField(max_length=100)
    fname = models.CharField(max_length=50)
    mname = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)

    class Meta:
        db_table = "student"





