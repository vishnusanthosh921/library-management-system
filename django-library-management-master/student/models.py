from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Department(models.Model):
    name=models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
class Student(models.Model):
    first_name=models.CharField(max_length=120,null=True,blank=True)
    last_name=models.CharField(max_length=120,null=True,blank=True)
    department=models.ForeignKey(Department,on_delete=models.CASCADE,null=True,blank=True)
    student_id=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        last_4_digits=self.student_id.username[-4:]
        return "{}_{}-{}".format(self.first_name,last_4_digits,self.department)
    

    