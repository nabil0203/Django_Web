from django.shortcuts import render, redirect, get_object_or_404

from . import models, forms

from django.contrib import messages

from django.db import connection

from django.db.models import Count,Avg,Max,Min,Sum




# Create your views here.




def list_students(request):
    student_app = models.Student.objects.all()

# O(n+1) query problem solution:
    student_app_optimized = models.Student.objects.select_related('department').all()           # O(1)

#optimization
    # one_to_many_opt = models.Student.objects.select_related('department').all()
    # many_to_many_opt = models.Student.objects.prefetch_related('course').all()



#order by
    # course = models.Course.objects.order_by('id').all()
    # for i in course:
    #     print(i.id,i.title)


# raw sql
    # students = models.Student.objects.raw("""SELECT * FROM student_student""")
    # this is so complex and we normally don't use it


    
# connection related sql
    # cursor = connection.cursor()
    # cursor.execute("""SELECT * FROM student_student""")
    # rows = cursor.fetchall()
    # print(rows)


# Aggregation
    total_student = models.Student.objects.aggregate(total = Count('id'))
    print(total_student)


# Annotation:

    student_annotate = models.Student.objects.annotate(student_count = Count('id'))

    for i in student_annotate:
        print(i.name,i.department,i.student_count)

    print(student_annotate)



    return render(request, "student_list.html", {"students": student_app})









# --------------Model Form--------------
def create_students(request):
    if request.method == "POST":
        form = forms.StudentForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "New Student Created Successfully")
            return redirect(list_students)

    form = forms.StudentForm()
    return render(request, 'student_create.html', {'form' : form})






def update_students(request, id):

    student_app = get_object_or_404(models.Student, id=id)
    
    if request.method == "POST":
        form = forms.StudentForm(request.POST, instance=student_app)

        if form.is_valid():
            form.save()
            messages.success(request, "Student's Information updated Successfully")
            return redirect(list_students)

    
    form = forms.StudentForm(request.POST or None, instance=student_app)
    return render(request, 'student_create.html', {'form' : form, 'isUpdated' : True})






def delete_students(request, id):
    student_app = get_object_or_404(models.Student, id=id)
    
    student_app.delete()
    messages.success(request, "Student Deleted Successfully")
    return redirect('list_students')



