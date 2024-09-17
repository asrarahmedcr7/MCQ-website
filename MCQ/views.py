from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views import generic
from django.http import Http404
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

def calculate_result(request, quiz_id):
    if request.method == "POST":
        score = 0
        qsns = Question.objects.filter(quiz_id=quiz_id)
        for qsn in qsns:
            choice = request.POST.get(f'question_{qsn.id}')
            if Choice.objects.get(pk = choice).is_answer:
                score += 1
        return render(request, 'MCQ/result.html', {"score":score})
    return Http404()



