from django.shortcuts import render
from .models import Question, Choice
# Create your views here.

def quiz(request):
    print("hello")
    questions = Question.objects.all().prefetch_related('choices')
    
    if request.method == "POST":
        score = 0
        print(request.POST)
        for question in questions:
            selected = request.POST.get(str(question.id))  # {1: 2, 2: 3}
            correct = Choice.objects.filter(id=selected, is_correct=True).exists()

            if correct:
                score += 1
           
        return render(request, 'quiz/score.html', context={
            'total_question': len(questions),
            'score': score
        })


    return render(request, 'quiz/quiz.html', context={
        'questions': questions
    })