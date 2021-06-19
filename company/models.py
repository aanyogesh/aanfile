from django.db import models

# Create your models here.
class Company(models.Model):
     name = models.CharField(max_length=200)
     location = models.CharField(max_length=200)
     phone = models.IntegerField(default=0)
     created_at = models.DateTimeField('created_at')
     update_at = models.DateTimeField('update_at')

     def __str__(self):
          return self.name

class Client(models.Model):
     company = models.ForeignKey(Company, on_delete=models.CASCADE)
     name = models.CharField(max_length=200)
     location = models.CharField(max_length=200)
     
     def __str__(self):
          return self.name
          