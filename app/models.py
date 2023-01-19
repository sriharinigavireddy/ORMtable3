from django.db import models

# Create your models here.
class Country(models.Model):
    name=models.CharField(max_length=50)

class Capital(models.Model):
    cname=models.OneToOneField('country',on_delete=models.CASCADE)