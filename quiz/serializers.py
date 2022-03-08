from rest_framework import serializers
from .models import Category, Quiz

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            "id",
            "name"
        )
        
class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = (
            "id",
            "title",
            "date_created",
            "category_id"
        )