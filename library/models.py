from django.db import models

# Create your models here.
class student(models.Model):
    first_name=models.CharField(max_length=122)
    last_name=models.CharField(max_length=122)
    faculty=models.CharField(max_length=122)
    semester=models.CharField(max_length=122)

    def __str__(self):
        return self.first_name,self.last_name
