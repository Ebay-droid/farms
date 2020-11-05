from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from . import serializers
from .models import *
from django.http import Http404
from datetime import datetime

from rest_framework import status

# Create your views here.
class Farms(APIView):
  
  def get(self,request):
    farms = Farm.objects.all()
    serializer = serializers.FarmSerializer(farms, many=True)
    return Response(serializer.data)
  
  
  def post(self,request):
    serializer = serializers.FarmSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
  
class FarmDetail(APIView):
  def get(self,request,farm_id):
    try:
      farm = Farm.objects.get(pk=farm_id)
      
    except Farm.DoesNotExist:
      raise Http404    
    serializer = serializers.FarmSerializer(farm)
    return Response(serializer.data) 
  
  def delete(self, request, farm_id):
      try:
          farm = Farm.objects.get(pk=farm_id)
      except Farm.DoesNotExist:
          raise Http404
      farm.delete()
      return Response(status=status.HTTP_204_NO_CONTENT)


class Animal(APIView):
  
  def get(self,request,farm_id):
    animals = Animals.objects.filter(farm_id=farm_id)
    serializer = serializers.AnimalSerializer(animals, many=True)
    return Response(serializer.data)
  
  
  def post(self,request,farm_id):
    try:
      Farm.objects.get(pk=farm_id)
    except Farm.DoesNotExist:
      raise Http404
    
    serializer=serializers.AnimalSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save(farm_id=farm_id)  
      return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class AnimalDetail(APIView):
  def get(self,request,farm_id,animal_id):
    try:
      animal = Animals.objects.get(farm_id=farm_id,pk=animal_id)
      
    except Animals.DoesNotExist:
      raise Http404    
    serializer = serializers.AnimalSerializer(animal)
    return Response(serializer.data) 
  
  def delete(self, request, farm_id, animal_id):
      try:
          animal = Animals.objects.get(pk=animal_id, farm_id=farm_id)
      except Animals.DoesNotExist:
          raise Http404
      animal.delete()
      return Response(status=status.HTTP_204_NO_CONTENT)   