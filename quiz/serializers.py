from rest_framework import serializers
from .models import Category, Quiz

class CategorySerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    category_counts = serializers.SerializerMethodField()
    class Meta:
        model = Category
        fields = (
            "category",
            "category_counts"
        )
    def get_counts(self, obj):        
        return obj.category.count()
        
class QuizSerializer(serializers.ModelSerializer):
    # quiz= serializers.StringRelatedField(many=True)
    # quiz_count = serializers.SerializerMethodField()
    
    class Meta:
        model = Quiz
        fields = (
            "id",
            # "quiz",
            "title",
            # "quiz_count"
        )
        
    # def get_quiz_count(self, obj):        
        # return obj.quiz.count()