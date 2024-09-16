from django.db import models

class Quiz(models.Model):
    title = models.CharField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
class Question(models.Model):
    quiz = models.ForeignKey(Quiz, related_name='questions', on_delete=models.CASCADE)
    question_text = models.TextField()
class Choice(models.Model):
    question = models.ForeignKey(Question, related_name='answers', on_delete=models.CASCADE)
    choice_text = models.TextField()
    is_answer = models.BooleanField(default=False)

# Question:
# Text
#   Choice:
#       Text