from django.shortcuts import render
from .serializers import CategorySerializer, QuizSerializer
from rest_framework import viewsets, generics
from .models import Category, Quiz
from rest_framework.views import APIView
# from .permissions import IsStuffOrReadOnly

class QuizListView(generics.ListAPIView):
    queryset= Quiz.objects.all()
    serializer_class = QuizSerializer

class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    # permission_classes = (IsStuffOrReadOnly,)
    
    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_staff:
            return queryset

# class QuizView(viewsets.ModelViewSet):
#      queryset = Quiz.objects.all()
     
#      def get_queryset(self):
#         queryset = super().get_queryset()
#         if self.request.user.is_staff:
#             return queryset
