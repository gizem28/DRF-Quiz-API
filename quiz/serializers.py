from rest_framework import serializers
from .models import Category, Quiz

class QuizSerializer(serializers.ModelSerializer):
    question = serializers.StringRelatedField(many=True)
    question_count = serializers.SerializerMethodField()
    
    class Meta:
        model = Quiz
        fields = (
            "title",
            "question",
            "question_count"
        )
        
        def get_question_count(self, obj):        
             return obj.question.count()
        
class CategorySerializer(serializers.ModelSerializer):
    quiz = serializers.StringRelatedField(many=True)
    quiz_count = serializers.SerializerMethodField()
    class Meta:
        model = Category
        fields = (
            "id",
            "category",
            "quiz",
            "quiz_count"
        )
    def get_quiz_count(self, obj):        
        return obj.quiz.count()
        
