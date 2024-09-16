from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views import generic
from .models import Quiz, Question, Choice

class index(generic.ListView):
    context_object_name = "quizzes"
    template_name = 'MCQ/index.html'

    def get_queryset(self) -> QuerySet[Any]:
        return Quiz.objects.all()

class quiz(generic.DetailView):
    model = Quiz
    template_name = 'MCQ/Quiz.html'

class result(generic.DetailView):
    model = Quiz
    template_name = 'MCQ/result.html'
