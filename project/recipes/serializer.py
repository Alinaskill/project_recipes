from .models import *
from rest_framework import serializers


class RecipeSerializer(serializers.ModelSerializer):
   class Meta:
       model = Recipe
       fields = ['id', 'name', 'description']


class CategorySerializer(serializers.ModelSerializer):
   class Meta:
       model = Category
       fields = ['id', 'name']
