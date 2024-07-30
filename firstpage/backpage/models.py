from django.db import models


# Create your models here.
class page(models.Model):
  firstname = models.CharField(max_length=100)
  lastname = models.CharField(max_length=255)
  Address1 = models.CharField(max_length=255)
  Address2 = models.CharField(max_length=255)
  Email = models.CharField(max_length=255)
  State = models.CharField(max_length=255)
  Phn_no = models.IntegerField()
  City = models.CharField(max_length=100)
  Zip = models.IntegerField()


  
  

  


