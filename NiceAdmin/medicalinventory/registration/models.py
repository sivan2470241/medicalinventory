from django.db import models


class Qualification(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):

        
        return self.name
 
class specializations(models.Model):
    name1 = models.CharField(max_length=100)
    def __str__(self):
        
        
        return self.name1


class Registration(models.Model):

    registration_id = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile = models.CharField(max_length=20)
    highest_qualification = models.ForeignKey('Qualification', on_delete=models.CASCADE)
    specialized_subject = models.ForeignKey('specializations', on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='photos/', max_length=200)
    resume = models.FileField(upload_to='resumes/', max_length=500)
   
    def __str__(self):
        
        return self.name


