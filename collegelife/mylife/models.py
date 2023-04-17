from django.db import models

# Create your models here.
class Mylife (models.Model):
    age=models.CharField(max_length=112)
    topic=models.CharField(max_length=112)
    college=models.CharField(max_length=112)
    school=models.CharField(max_length=112)
    rollno=models.CharField(max_length=112)
    