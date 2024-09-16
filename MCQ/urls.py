from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="index"),
    path('/<int:pk>/quiz', views.quiz, name="quiz"),
    path('/<int:pk>/result', views.result, name="result"),
]