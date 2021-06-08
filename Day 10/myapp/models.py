from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    course = models.CharField(max_length=50)
    gender = models.BooleanField(default=False)
    fees = models.IntegerField()

    def __str__(self):
        return self.first_name

class Heroes(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    powers = models.CharField(max_length=50)
    gender = models.BooleanField(default=False)
   
    def __str__(self):
        return self.first_name