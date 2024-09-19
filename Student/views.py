from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views import generic
from django.http import Http404, HttpResponseRedirect
from .models import Quiz, Question, Choice
from datetime import datetime

class index(generic.ListView):
    context_object_name = "quizzes"
    template_name = 'Student/index.html'

    def get_queryset(self) -> QuerySet[Any]:
        return Quiz.objects.all()

class quiz(generic.DetailView):
    model = Quiz
    template_name = 'Student/Quiz.html'

class result(generic.DetailView):
    model = Quiz
    template_name = 'Student/result.html'

def calculate_result(request, quiz_id):
    if request.method == "POST":
        score = 0
        qsns = Question.objects.filter(quiz_id=quiz_id)
        for qsn in qsns:
            choice = request.POST.get(f'question_{qsn.id}')
            if Choice.objects.get(pk = choice).is_answer:
                score += 1
        return render(request, 'Student/result.html', {"score":score})
    return Http404()

def createQuiz(request):
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        created_at = datetime.now()
        new_quiz = Quiz(title = title, description = description, created_at = created_at)
        new_quiz.save()
        return HttpResponseRedirect(f'{new_quiz.id}/questions')
    return Http404()

def createQuestion(request, quiz_id):
    quiz = Quiz.objects.get(pk=quiz_id)
    
    return render(request, 'Student/quiz.html', {"quiz":quiz})