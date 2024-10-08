from django.db import models
from core.models import CustomUser
class Quiz(models.Model):

    def __str__(self) -> str:
        return self.title

    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Question(models.Model):

    def __str__(self) -> str:
        return self.question_text

    quiz = models.ForeignKey(Quiz, related_name='questions', on_delete=models.CASCADE)
    question_text = models.TextField()
    
class Choice(models.Model):

    def __str__(self) -> str:
        return self.choice_text

    question = models.ForeignKey(Question, related_name='answers', on_delete=models.CASCADE)
    choice_text = models.TextField()
    is_answer = models.BooleanField(default=False)

class Result(models.Model):

    def __str__(self) -> str:
        return self.user.username + ' ' + self.quiz.title

    user = models.ForeignKey(CustomUser, related_name="results", on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, related_name="quizzes", on_delete=models.CASCADE)
    user_choices_json = models.JSONField(default=dict)

    
# Question:
# Text
#   Choice:
#       Text