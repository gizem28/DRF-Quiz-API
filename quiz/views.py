from django.shortcuts import render
from .serializers import CategorySerializer, QuizSerializer
from rest_framework import viewsets, generics
from .models import Category, Quiz
from rest_framework.views import APIView
# from .permissions import IsStuffOrReadOnly

class QuizListView(generics.ListAPIView):
    queryset=Category.objects.all()
    serializer_class = CategorySerializer

class QuizRead(generics.ListAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    # permission_classes = (IsStuffOrReadOnly,)
    
    def get_queryset(self):
        category = self.kwargs['category'].capitalize()
        return Quiz.objects.filter(category__name=category)
        
        # if self.request.user.is_staff:
        #     return queryset
