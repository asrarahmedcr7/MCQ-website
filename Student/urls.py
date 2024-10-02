from django.urls import path
from . import views
from core.views import student_login_view

app_name = "Student"

urlpatterns = [
    path('home', views.index.as_view(), name="index"),
    path('<int:pk>/quiz', views.quiz.as_view(), name="quiz"),
    path('quiz/<int:quiz_id>/result/', views.calculate_result, name='calculate_result'),
]