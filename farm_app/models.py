from django.db import models

# Create your models here.
class Farm(models.Model):
  name =models.CharField(max_length=30,unique=True)  
  location = models.CharField(max_length=30)
  livestock = models.CharField(max_length=20,choices=[('poultry','poultry'),('cows','cows'),('sheep','sheep'),('goats','goats')])
  animal_count = models.IntegerField()
  manager = models.CharField(max_length=30)

  def __str__(self):
    return self.name
  
  
class Animals(models.Model):
  farm = models.ForeignKey(Farm,on_delete=models.CASCADE)  
  name = models.CharField(max_length=20)
  animal_type = models.CharField(max_length=20,choices=[('poultry','poultry'),('cows','cows'),('sheep','sheep'),('goats','goats')])
  date_of_birth = models.DateTimeField(blank=True)
  date_inseminated = models.DateTimeField(blank=True)
  check_date = models.DateTimeField(blank=True)
  due_date = models.DateTimeField(blank=True)