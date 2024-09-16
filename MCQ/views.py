from django.shortcuts import render
from django.views import generic
from .models import Quiz, Question, Choice

class index(generic.DetailView):
    model = Quiz
    template_name = 'MCQ/index.html'

class quiz(generic.DetailView):
    model = Quiz
    template_name = 'MCQ/Quiz.html'

class result(generic.DetailView):
    model = Quiz
    template_name = 'MCQ/result.html'
