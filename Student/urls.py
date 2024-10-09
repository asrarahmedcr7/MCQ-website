from django.urls import path
from . import views
from core.views import student_login_view

app_name = "Student"

urlpatterns = [
    path('home', views.index.as_view(), name="index"),
    path('<int:quiz_id>/quiz', views.quizView, name="quiz"),
    path('quiz/<int:quiz_id>/result/', views.calculate_result, name='calculate_result'),
    path('leaderboard', views.leaderboardView, name='leaderboard'),
]