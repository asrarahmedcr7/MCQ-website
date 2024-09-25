from django.shortcuts import render, redirect
from Student.models import Quiz, Question
from datetime import datetime
from django.http import Http404, JsonResponse
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from .forms import QuizForm

@login_required(login_url='Teacher:login')
def home(request):
    quiz_list = Quiz.objects.order_by('created_at')[::-1]
    return render(request, 'Teacher/home.html', {"quiz_list":quiz_list, 'QuizForm':QuizForm})

def createQuiz(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        quiz = Quiz(title = title, description = description, created_at = datetime.now())
        quiz.save()
        return redirect("Teacher:home")
    return Http404()

def editQuiz(request, quiz_id):
    if request.method == "POST":
        quiz = Quiz.objects.get(pk=quiz_id)
        quiz.title = request.POST.get(f"quiz_title_{quiz_id}")
        quiz.description = request.POST.get(f"quiz_description_{quiz_id}")
        quiz.save()
        return redirect("Teacher:home")
    return

def deleteQuiz(request, quiz_id):
    quiz = Quiz.objects.get(pk = quiz_id)
    quiz.delete()
    return JsonResponse({
        "message":"Success",
    })

def showQuestions(request, quiz_id):
    quiz = Quiz.objects.get(pk = quiz_id)
    return render(request, 'Teacher/questions.html', {'quiz':quiz})

class TeacherLoginView(LoginView):
    template_name = 'Teacher/login.html'
    redirect_authenticated_user = False
    def get_success_url(self):
        return reverse_lazy('Teacher:home')

class TeacherLogoutView(LogoutView):
    next_page = reverse_lazy('Teacher:login')

def editQuestion(request, question_id, quiz_id):
    if request.method == "POST":
        question = Quiz.objects.get(pk=quiz_id).questions.all().get(pk=question_id)
        question.question_text = request.POST.get(f'question_text_{question_id}')
        for choice in question.answers.all():
            choice.choice_text = request.POST.get(f'choice_{choice.id}')
            choice.save()
        question.save()
        return render(request, 'Teacher/editQuiz.html', {'quiz':Quiz.objects.get(pk = quiz_id), 'message':f'Question {question_id} Edited'})
    return Http404

def editQuestions(request, quiz_id):
    if request.method == "POST":
        return render(request, 'Teacher/editQuiz.html', {'quiz':Quiz.objects.get(pk = quiz_id),})
    return Http404()