# Generated by Django 4.0.2 on 2022-03-10 22:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0011_alter_question_difficulty_alter_question_quiz_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answer', to='quiz.question'),
        ),
        migrations.AlterField(
            model_name='question',
            name='difficulty',
            field=models.CharField(choices=[('L', 'Low'), ('H', 'High'), ('M', 'Medium')], max_length=50),
        ),
    ]
