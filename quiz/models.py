from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    
class Quiz(models.Model):
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, related_name="quiz")
    title = models.CharField(max_length=200)
    date_created =  models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'Quizzes'
    
class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.DO_NOTHING, related_name="question")
    updated_date = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=100)
    levels = {
        ("H", "High"),
        ("M", "Medium"),
        ("L", "Low"),
    }
    difficulty= models.CharField(max_length=50, choices=levels)
    date_created =  models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.DO_NOTHING, related_name="answer")
    updated_date = models.DateTimeField(auto_now=True)
    answer = models.TextField(max_length=225, null=True)
    is_right = models.BooleanField(default=False)
    
    def __str__(self):
        return self.answer