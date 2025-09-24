from django.shortcuts import render

from . import models

# Create your views here.

def list_students(request):
    students = models.Student.objects.all()
    return render(request, 'student_list.html', {'students' : students})


def create_students(request):
    return render(request, 'student_create.html')

