from django.shortcuts import render, redirect, get_object_or_404

from . import models, forms

from django.contrib import messages

from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy




# Create your views here.



# -----------------Function based view--------------
# def list_students(request):
#     student_app = models.Student.objects.all()
#     return render(request, "student_list.html", {"students": student_app})



# --------------------Class based view-----------------
class StudentViewList(ListView):
    template_name = 'student_list.html'
    model = models.Student
    context_object_name = 'students'



# --------------------------------------------------------------------------------------------------






# -----------------Function based view-------------------


# ----------HTML Form--------------
# def create_students(request):
    # if request.method == 'POST':
    #     name = request.POST.get('name')
    #     email = request.POST.get('email')
    #     age = request.POST.get('age')

    #     models.Student.objects.create(
    #         name = name,
    #         email = email,
    #         age = age
    #     )

    #     return redirect(list_students)



# --------------Model Form--------------
# def create_students(request):
    # if request.method == "POST":
    #     form = forms.StudentForm(request.POST)

    #     if form.is_valid():
    #         form.save()
    #         messages.success(request, "New Student Created Successfully")
    #         return redirect(list_students)

    # form = forms.StudentForm()
    # return render(request, 'student_create.html', {'form' : form})





# --------------------Class based view-----------------

class StudentCreateView(CreateView):
    model = models.Student
    form_class = forms.StudentForm
    template_name = 'student_create.html'
    success_url = reverse_lazy('list_students')
    
    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        messages.success(self.request,'Student added successfully!')
        return super().form_valid(form)





# --------------------------------------------------------------------------------------------------




# -----------------Function based view-------------------

# def update_students(request, id):

#     student_app = get_object_or_404(models.Student, id=id)
    
#     if request.method == "POST":
#         form = forms.StudentForm(request.POST, instance=student_app)

#         if form.is_valid():
#             form.save()
#             messages.success(request, "Student's Information updated Successfully")
#             return redirect(list_students)

    
#     form = forms.StudentForm(request.POST or None, instance=student_app)
#     return render(request, 'student_create.html', {'form' : form, 'isUpdated' : True})




# --------------------Class based view-----------------
class StudentUpdateView(UpdateView):
    model = models.Student
    form_class = forms.StudentForm
    template_name = 'student_create.html'
    success_url = reverse_lazy('list_students')
    pk_url_kwarg = 'id'
    
    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        messages.success(self.request,'Student updated successfully!')
        return super().form_valid(form)






# --------------------------------------------------------------------------------------------------




# -----------------Function based view-------------------

# def delete_students(request, id):
#     student_app = get_object_or_404(models.Student, id=id)
    
#     student_app.delete()
#     messages.success(request, "Student Deleted Successfully")
#     return redirect('list_students')




# --------------------Class based view-----------------
class StudentDeleteView(DeleteView):
    model = models. Student
    template_name ='student_delete.html'
    success_url = reverse_lazy('list_students')
    pk_url_kwarg = 'id'

    def delete(self, request, *args, ** kwargs):
        messages.success(self.request, 'Student deleted Successfully')
        return super().delete(request, *args, ** kwargs)
    
