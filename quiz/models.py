from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
class Quiz(models.Model):
    quiz = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    date_created =  models.DateTimeField(auto_now_add=True)
    category_id = models.IntegerField()
    def __str__(self):
        return self.title
    
class Question(models.Model):
    updated_date = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=100)
    diffuculty