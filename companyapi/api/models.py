from django.db import models

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=50)
    company_id = models.AutoField(primary_key=True)
    location = models.CharField(max_length=50)
    about = models.TextField()
    type = models.CharField(max_length=100,choices=(('IT','IT'),('NON IT','NON IT'),("Pharma","Pharma")))
    added_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name + '----' + self.location


# emp models
class Employee(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=10)
    about = models.TextField()
    position = models.CharField(max_length=50,choices=(
        ('Manager','Manager'),
        ('SDE','SDE'),
        ('Project Leader','PL'),
    ))
    
    company = models.ForeignKey(Company,on_delete=models.CASCADE)
    
    
    
