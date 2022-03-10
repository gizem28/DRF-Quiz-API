from rest_framework import serializers
from .models import Category, Quiz, Answer, Question

class AnswerSerializer(serializers.ModelSerializer):
       class Meta:
        model = Answer
        fields = ('answer', 'is_right')
        
class QuestionSerializer(serializers.ModelSerializer):
    answer = AnswerSerializer(many=True)

    class Meta:
        model = Question
        fields = ('title', 'answer', 'difficulty',)

class QuizSerializer(serializers.ModelSerializer):
    question= QuestionSerializer(many=True, write_only=True)
    # question_count = serializers.SerializerMethodField()
    class Meta:
        model = Quiz
        fields = (
            "title",
            "question",
            # "question_count"
        )
        
        # def get_question_count(self, obj):        
        #     return obj.question.count()
        
class CategorySerializer(serializers.ModelSerializer):
    quiz = QuizSerializer(many=True, write_only=True)
    quiz_count = serializers.SerializerMethodField()
    # category = serializers.StringRelatedField()
    class Meta:
        model = Category
        fields = (
            "id",
            "name",
            "quiz",
            # "category",
            "quiz_count"
        )
    def get_quiz_count(self, obj):        
        return obj.quiz.count()
        
