from django.shortcuts import render, redirect, get_object_or_404

from . import models, forms

from django.contrib import messages




# Create your views here.



# -----------------Function based view--------------
def list_students(request):
    student_app = models.Student.objects.all()
    return render(request, "student_list.html", {"students": student_app})






# -----------------Function based view-------------------



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





# -----------------Function based view-------------------

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





# -----------------Function based view-------------------

def delete_students(request, id):
    student_app = get_object_or_404(models.Student, id=id)
    
    student_app.delete()
    messages.success(request, "Student Deleted Successfully")
    return redirect('list_students')



