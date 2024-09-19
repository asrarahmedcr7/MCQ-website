from django.db import models

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

# Question:
# Text
#   Choice:
#       Text