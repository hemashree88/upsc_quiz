from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('category/', views.category, name='category'),
    path('count/', views.question_count, name='question_count'),
    path('quiz/', views.quiz_page, name='quiz_page'),
]
