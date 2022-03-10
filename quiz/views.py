from django.shortcuts import render
from .serializers import CategorySerializer, QuizSerializer, QuestionSerializer
from rest_framework import viewsets, generics
from .models import Category, Quiz, Answer, Question
from rest_framework.views import APIView
# from .permissions import IsStuffUser

class QuizListView(generics.ListAPIView):
    queryset=Category.objects.all()
    serializer_class = CategorySerializer

class QuizRead(generics.ListAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    # permission_classes = (IsStuffUser)
    # pagination_class=PageNumPagi questionread ekle
    # filter_backends= [DjangoFilterBackend] questionread ekle
    # filterset_fields= ['diffuculty']
    
    def get_queryset(self):
        category = self.kwargs['category'].capitalize()
        return Quiz.objects.filter(category__name=category)
        
        # if self.request.user.is_staff:
        #     return queryset
        

class QuestionRead(generics.ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    def get_queryset(self):
        quiz = self.kwargs['quiz'].capitalize()
        return Question.objects.filter(quiz__title=quiz)