from django.db import models

# Create your models here.


class old_ques(models.Model):
    faculty = models.CharField(max_length=255)
    semester = models.CharField(max_length=255)

    class meta : 
        ordering = ['year']



