from .serializer import *
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render

class RecipeView(APIView):
    def get(self, request):
        output = [
            {
                "name": output.name,
                "description": output.description,
                "category": output.category
            } for output in Recipe.objects.all()
        ]
        return Response(output)

    def post(self, request):
        serializer = RecipeSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

class CategoryView(APIView):
    def get(self, request):
        output = [
            {
                "name": output.name,
            } for output in Category.objects.all()
        ]
        return Response(output)

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
