from django.db import models

# Create your models here.
class ContactModel(models.Model):
    firstname=models.CharField(max_length=255)
    lastname=models.CharField(max_length=255)
    email=models.EmailField(null=True)
    message=models.CharField(max_length=1000)

    objects= models.Manager