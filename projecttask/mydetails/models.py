from django.db import models

# Create your models here.
class Ourdetails(models.Model):
    name = models.CharField(max_length=200)
    department = models.CharField(max_length=200)
    collegename= models.TextField(max_length=200)
    contactnumber=models.IntegerField()
    yearofjoining=models.DateField(auto_now_add=True)
    passoutyear= models.TimeField(null=True, default=None)
    emailId=models.EmailField()
class Meta:
    db_table='my_user'
    

