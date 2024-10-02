from django.urls import path
from . import views
app_name = 'core'

urlpatterns = [
    path('', views.homeview, name="home"),
    path('teacher/login', views.teacher_login_view, name="teacher-login"),
    path('student/login', views.student_login_view, name="student-login"),
    path('logout', views.CoreLogoutView.as_view(), name='logout'),
]