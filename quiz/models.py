from django.db import models

# Create your models here.
class Category(models.Model):
    category = models.CharField(max_length=100)
    def __str__(self):
        return self.category
    
class Quiz(models.Model):
    quiz = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    date_created =  models.DateTimeField(auto_now_add=True)
    id = models.IntegerField(primary_key=True)
    def __str__(self):
        return self.title
    
class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    updated_date = models.DateTimeField(auto_now=True)
    question = models.CharField(max_length=100)
    levels = {
        ("H", "High"),
        ("M", "Medium"),
        ("L", "Low"),
    }
    diffuculty= models.CharField(max_length=50, choices=levels)
    date_created =  models.DateTimeField(auto_now_add=True)
    # quiz_id = models.IntegerField()
    
    def __str__(self):
        return self.question
    
class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    updated_date = models.DateTimeField(auto_now=True)
    choice1 = models.CharField(max_length=200)
    choice2 = models.CharField(max_length=200)
    choice3 = models.CharField(max_length=200)
    choice4 = models.CharField(max_length=200)
    answer= {
        ("A", "A"),("B", "B"), ("C", "C"), ("D", "D")
    }
    is_right = models.CharField(max_length=50, choices=answer)
    # question_id= models.IntegerField()
    
    def __str__(self):
        return self.choice1 , self.choice2 , self.choice3 , self.choice4