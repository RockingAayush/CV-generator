from django.db import models

# Create your models here.
class Profile(models.Model):

    def __str__(self):
        return self.name

    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    summary = models.TextField(max_length=2000)
    degree = models.CharField(max_length=200)
    branch = models.CharField(max_length=200,default='Empty')
    cgpa = models.FloatField(max_length=200,default=0)
    school = models.CharField(max_length=200)
    university = models.CharField(max_length=200)
    previous_work = models.TextField(max_length=2000)
    skills = models.TextField(max_length=2000)
    