from django.db import models

# Create your models here.
class student(models.Model):
    username=models.CharField(max_length=10)
    section=models.CharField(max_length=5)
    year=models.IntegerField()
    photo=models.FileField(upload_to='images/')
    nots=models.BooleanField(blank=True,null=True)
    accept=models.BooleanField(blank=True,null=True)
    declane=models.BooleanField(blank=True,null=True)
    def __str__(self):
        return self.username

class Reports(models.Model):
    username=models.CharField(max_length=10)
    branch=models.CharField(max_length=8)
    date=models.DateField()
    subject=models.TextField()
    reason=models.TextField()

    def __str__(self):
        return self.username

class prof(models.Model):
    username=models.EmailField(null=True)
    branch=models.CharField(max_length=10)
    photo=models.FileField(upload_to='images/')

    def __str__(self):
        return self.username
    

    
