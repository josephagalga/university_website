from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fullName = models.CharField(max_length=50)
    password = models.CharField(max_length=10)
    email = models.EmailField()
    phone = models.CharField(max_length=11)
    dob = models.DateField()
    gender = models.CharField(max_length=7)
    streetAddress = models.CharField(max_length=100)
    city = models.CharField(max_length=20)
    region = models.CharField(max_length=20)
    district = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    previousSchool = models.CharField(max_length=50)
    gpa = models.FloatField()
    programOfInterest = models.CharField(max_length=100)
    sop = models.CharField(max_length=100)
    emergencyName = models.CharField(max_length=50)
    emergencyPhone = models.CharField(max_length=10)

    def ___str__(self):
        return self.name