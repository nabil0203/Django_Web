from django.urls import path
from .views import quiz
# from quiz.views import quiz

urlpatterns = [
    path('', quiz, name='quiz')
]
