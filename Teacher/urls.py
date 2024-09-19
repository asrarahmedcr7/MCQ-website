from django.urls import path
from . import views

app_name = "Teacher"

urlpatterns = [
    path('home', views.home, name="home"),
    path('createQuiz', views.createQuiz, name="createQuiz"),
]