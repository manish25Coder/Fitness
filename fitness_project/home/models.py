from django.db import models

# Create your models here.
class Contact(models.Model):
    sno=models.AutoField(primary_key=True)
    name=models.CharField(max_length=30)
    email=models.CharField(max_length=50)
    phone=models.CharField(max_length=10)
    desc=models.TextField()
    date=models.DateField(auto_now_add=True,blank=True)

    def __str__ (self):
        return "Message from " + self.name #+ ' - ' + self.email

class Signup(models.Model):
    email=models.CharField(max_length=50)

    def __str__ (self):
        return "Message from " + self.name



