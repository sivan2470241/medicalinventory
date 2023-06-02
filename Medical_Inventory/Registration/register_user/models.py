from django.db import models

# Create your models here.

class Qualification(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class Subject(models.Model):
    qualification = models.ForeignKey(Qualification,on_delete=models.CASCADE)
    subjects=models.CharField(max_length=150)


    def __str__(self):
        return self.subjects

class User(models.Model):
    registration_id = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile = models.CharField(max_length=15)
    highest_qualification = models.ForeignKey(Qualification, on_delete=models.SET_NULL,blank=True,null=True)
    specialized_subject = models.ForeignKey(Subject, on_delete=models.SET_NULL,blank=True,null=True)
    photo = models.ImageField(upload_to='photos/')
    resume = models.FileField(upload_to='resumes/')
    updated_at=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name
