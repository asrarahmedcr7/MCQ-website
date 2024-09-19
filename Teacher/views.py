from django.shortcuts import render, redirect
from Student.models import Quiz
from datetime import datetime
from django.http import Http404

def home(request):
    quiz_list = Quiz.objects.all()
    return render(request, 'Teacher/home.html', {"quiz_list":quiz_list})

def createQuiz(request):
    if request.method == "POST":
        title = request.POST.get("quiz_title")
        description = request.POST.get("quiz_description")
        quiz = Quiz(title = title, description = description, created_at = datetime.now())
        quiz.save()
        return redirect("Teacher:home")
    return Http404()