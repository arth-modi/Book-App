from django.db import models
from datetime import date

# Create your models here.
class Users(models.Model):
    email = models.EmailField(max_length=100)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    
    def __str__(self):
        return (self.first_name + self.last_name)
    
class Authors(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    telephone = models.PositiveIntegerField(max_length=10)
    address = models.TextField(max_length=255)
    author = models.ManyToManyField("self")
    followers = models.ForeignKey(Users, on_delete=models.CASCADE)
    
class Publishers(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    join_date = models.DateField(default=date.today())
    popularity_score = models.IntegerField()
    publisher = models.ManyToManyField("self")

    
class Books(models.Model):
    title = models.CharField(max_length=50)
    genre = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    published_date = models.DateField(default=date.today())
    author = models.ManyToManyField(Authors)
    publisher = models.ForeignKey(Publishers, on_delete=models.CASCADE)
    
    