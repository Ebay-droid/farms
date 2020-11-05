from rest_framework import serializers
from . import models
from django.conf import settings
import os


class FarmSerializer(serializers.ModelSerializer):
  
  class Meta:
    model = models.Farm
    fields = ['id','name','location','livestock','animal_count','manager']
    
    
class AnimalSerializer(serializers.ModelSerializer):
  
  class Meta:
    model = models.Animals
    fields = ['farm','name','animal_type','date_of_birth','date_inseminated','check_date','due_date']   