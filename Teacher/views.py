from django.shortcuts import render, redirect
from Student.models import Quiz, Question, Choice
from datetime import datetime
from django.http import Http404, JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from .forms import QuizForm

@login_required(login_url='core:teacher-login')
@never_cache
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

@never_cache
def showQuestions(request, quiz_id):
    quiz = Quiz.objects.get(pk = quiz_id)
    return render(request, 'Teacher/questions.html', {'quiz':quiz})

@never_cache
def editQuestion(request, question_id, quiz_id):
    if request.method == "POST":
        question = Quiz.objects.get(pk=quiz_id).questions.all().get(pk=question_id)
        question.question_text = request.POST.get(f'question_text_{question_id}')
        for choice in question.answers.all():
            choice.choice_text = request.POST.get(f'choice_{choice.id}')
            choice.save()
        question.save()
        return JsonResponse({
            'message':'Success',
        })
    return Http404()

def editQuestions(request, quiz_id):
    return render(request, 'Teacher/editQuiz.html', {'quiz':Quiz.objects.get(pk = quiz_id),})

def deleteChoice(request, choice_id, question_id, quiz_id):
    choice = Quiz.objects.get(pk = quiz_id).questions.get(pk=question_id).answers.get(pk=choice_id)
    choice.delete()
    return JsonResponse({
        "message":"Success",
    })

def addChoice(request, question_id, quiz_id):
    if request.method == "POST":
        choice_text = request.POST.get('new_choice_text')
        is_answer = request.POST.get('is_answer') == 'True'
        newChoice = Choice(question_id = question_id, choice_text = choice_text, is_answer = is_answer)
        newChoice.save()
        return JsonResponse({
            "message":"Success",
            'choice_text':choice_text,
            'choice_id':newChoice.id,
        })
    return Http404()

@never_cache
def addQuestion(request, quiz_id):
    question = Question(quiz_id = quiz_id, question_text = request.POST.get("new_question_text"))
    question.save()
    return redirect("Teacher:edit-questions", quiz_id=quiz_id)

def deleteQuestion(request, quiz_id, question_id):
    question = Quiz.objects.get(pk=quiz_id).questions.get(pk=question_id)
    question.delete()
    return JsonResponse({
        "message":"Success",
    })