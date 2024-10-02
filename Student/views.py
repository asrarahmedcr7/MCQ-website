from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views import generic
from django.http import Http404, HttpResponseRedirect
from .models import Quiz, Question, Choice
from datetime import datetime
from django.contrib.auth.mixins import LoginRequiredMixin

class index(LoginRequiredMixin, generic.ListView):
    context_object_name = "quizzes"
    template_name = 'Student/index.html'
    login_url = 'core:student-login'

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
        quiz = Quiz.objects.get(pk=quiz_id)
        user_choices = {}
        total_questions = 0
        for qsn in quiz.questions.all():
            selected = qsn.answers.get(pk = request.POST.get(f'question_{qsn.id}'))
            correct = qsn.answers.filter(is_answer=True).first()
            user_choices[qsn] = {
                'selected':selected,
                'correct':correct
            }
            if selected.is_answer:
                score += 1
            total_questions += 1
        return render(request, 'Student/result.html', {"score":score, 'user_choices':user_choices, 'score':score, 'total_questions':total_questions})
    return Http404()