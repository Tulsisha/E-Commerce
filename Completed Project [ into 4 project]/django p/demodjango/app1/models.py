from django.db import models

# Create your models here.
class contactform (models.Model):
    username=models.CharField( max_length=50)
    email=models.CharField( max_length=50)
    contact=models.CharField( max_length=50)
    address=models.CharField( max_length=100)
    pincode=models.CharField( max_length=100)
    message=models.CharField( max_length=100)
    def __str__(self):
        return self.username
class CPersonM (models.Model):
    cperson=models.CharField( max_length=50)
    email=models.CharField( max_length=50)
    contact=models.CharField( max_length=50)
    address=models.CharField( max_length=200)
    city=models.CharField( max_length=100)
    def _str_(self):
        return self.cperson

class CPersonM2 (models.Model):
    cperson=models.CharField( max_length=50)
    email=models.CharField( max_length=50)
    contact=models.CharField( max_length=50)
    address=models.CharField( max_length=200)
    city=models.CharField( max_length=100)
    def _str_(self):
        return self.cperson
        



    

    