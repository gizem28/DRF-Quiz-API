from django.contrib import admin
from .models import Category, Quiz, Question, Answer

admin.site.register(Category)
admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Answer)


# from django.contrib import admin
# from django.contrib.admin import TabularInline, StackedInline, site
# from super_inlines.admin import SuperInlineModelAdmin, SuperModelAdmin

# from .models import Answer, Question, Quiz,Category

# class AnswerInline(SuperInlineModelAdmin,admin.TabularInline):
#     model =Answer
#     extra = 4

# class QuestionInline(SuperInlineModelAdmin,admin.StackedInline):
#     model = Question
#     extra = 1
#     inlines = (AnswerInline,)

# class QuizAdmin(SuperModelAdmin):
#     model = Quiz
#     inlines = (QuestionInline,)

# # Register your models here.
# admin.site.register(Category)
# admin.site.register(Quiz,QuizAdmin)
# admin.site.register(Question)
# admin.site.register(Answer)
