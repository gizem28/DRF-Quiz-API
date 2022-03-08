from django.shortcuts import render
from .serializers import CategorySerializer, QuizSerializer
from rest_framework import viewsets
from .models import Category, Quiz
# from .permissions import IsStuffOrReadOnly

class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    # permission_classes = (IsStuffOrReadOnly,)
    
    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_staff:
            return queryset

