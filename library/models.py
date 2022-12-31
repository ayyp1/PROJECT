from django.db import models

# Create your models here.
class Books(models.Model):
    name = models.CharField(max_length=100)
    semester = models.CharField(max_length=50)
    faculty = models.CharField(max_length=50)