from django.db import models

# Create your models here. model is the DB, table product with these column
class Product(models.Model):
    desc = models.CharField(max_length=50,null=True,blank=True)
    price = models.DecimalField(max_digits=5,decimal_places=2)
    createdTime=models.DateTimeField(auto_now_add=True)
    fields =['desc','price']
    
    def __str__(self):
           return self.desc
       
class Student(models.Model):
    name = models.CharField(max_length=50)
    age = models.DecimalField(max_digits=3,decimal_places=0)
    email = models.EmailField(max_length=50,null=True,blank=True)
    image = models.ImageField(null=True,blank=True,default='/placeholder.png')
 
    def __str__(self):
           return self.name
       
class Task(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=100,null=True)
    completed = models.BooleanField(default=False,null=True)
   
    def __str__(self):
        return self.title
