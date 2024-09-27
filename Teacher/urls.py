from django.urls import path
from . import views

app_name = "Teacher"

urlpatterns = [
    path('home', views.home, name="home"),
    path('createQuiz', views.createQuiz, name="createQuiz"),
    path('<int:quiz_id>/editQuiz', views.editQuiz, name="editQuiz"),
    path('<int:quiz_id>/delete_quiz', views.deleteQuiz, name="delete_quiz"),
    path('<int:quiz_id>/show_questions', views.showQuestions, name="show_questions"),
    path('login', views.TeacherLoginView.as_view(), name="login"),
    path('logout', views.TeacherLogoutView.as_view(), name="logout"),
    path('<int:quiz_id>/editQuestions', views.editQuestions, name="edit-questions"),
    path('<int:quiz_id>/<int:question_id>/editQuestion', views.editQuestion, name="edit-question"),
    path('<int:quiz_id>/<int:question_id>/<int:choice_id>/delete-choice', views.deleteChoice, name="delete-choice"),
    path('<int:quiz_id>/<int:question_id>/add-choice', views.addChoice, name="add-choice"),
    path('<int:quiz_id>/addQuestion', views.addQuestion, name="add-question"),
]