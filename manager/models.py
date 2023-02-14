from django.db import models

# Create your models here.

class Department(models.Model):
    Name = models.CharField(max_length=50)
    year = models.IntegerField(max_length=50)
    Description = models.TextField(max_length=500)
    image = models.ImageField()

    def __str__(self):
        return self.Name

class DepartmentHead(models.Model):
    Name = models.CharField(max_length=50)
    Age = models.IntegerField(max_length=50)
    Employee_number = models.IntegerField(max_length=50)
    Description = models.TextField(max_length=500)
    image = models.ImageField()
    Department= models.ForeignKey(Department,on_delete=models.CASCADE)

    def __str__(self):
        return self.Name

class Employee(models.Model):
    Name = models.CharField(max_length=50)
    Age = models.IntegerField(max_length=50)
    Employee_number = models.IntegerField(max_length=50)
    Description = models.TextField(max_length=500)
    image = models.ImageField()
    Department= models.ForeignKey(Department,on_delete=models.CASCADE)
    Department_head= models.ForeignKey(DepartmentHead,on_delete=models.CASCADE)

    def __str__(self):
        return self.Name