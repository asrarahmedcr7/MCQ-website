from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render,redirect
from django.views import generic
from django.http import Http404
from .models import Quiz, Result
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.decorators.cache import never_cache

class index(LoginRequiredMixin, generic.ListView):
    context_object_name = "quizzes"
    template_name = 'Student/index.html'
    login_url = 'core:student-login'

    def get_queryset(self) -> QuerySet[Any]:
        quizzes = Quiz.objects.all().order_by('created_at')[::-1]
        quiz_list = []
        quiz_list_submitted = []
        user = self.request.user
        for quiz in quizzes:
            try:
                Result.objects.get(user_id = user.id, quiz_id = quiz.id)
                quiz_list_submitted.append(quiz)
            except:
                quiz_list.append(quiz)
        return {'quiz_list' : quiz_list, 'quiz_list_submitted':quiz_list_submitted}
    
@never_cache
def quizView(request, quiz_id):
    try:
        res = Result.objects.get(user_id = request.user.id, quiz_id = quiz_id)
        user_choices_json = res.user_choices_json
        score, total_questions = 0, 0
        for ans in user_choices_json.values():
            if ans['selected'] == ans['correct']:
                score += 1
            total_questions += 1
        return render(request, 'Student/standby.html', {'message':'You have already answered the quiz', 'user_choices_json' : user_choices_json, 'score':score, 'total_questions':total_questions})
    except:
        return render(request, 'Student/quiz.html', {'quiz':Quiz.objects.get(pk = quiz_id)})

class resultView(generic.DetailView):
    model = Quiz
    template_name = 'Student/result.html'

def calculate_result(request, quiz_id):
    if request.method == "POST":
        score = 0
        quiz = Quiz.objects.get(pk=quiz_id)
        user_choices, user_choices_json = {}, {}
        total_questions = 0
        for qsn in quiz.questions.all():
            selected = qsn.answers.get(pk = request.POST.get(f'question_{qsn.id}'))
            correct = qsn.answers.filter(is_answer=True).first()
            user_choices[qsn] = {
                'selected':selected,
                'correct':correct
            }
            user_choices_json[qsn.question_text] = {
                "selected": selected.choice_text,
                "correct" : correct.choice_text
            }

            if selected.is_answer:
                score += 1
            total_questions += 1
        res = Result(user_id = request.user.id, quiz_id = quiz_id, user_choices_json = user_choices_json)
        res.save()
        return render(request, 'Student/result.html', {"score":score, 'user_choices':user_choices, 'score':score, 'total_questions':total_questions})
    return Http404()