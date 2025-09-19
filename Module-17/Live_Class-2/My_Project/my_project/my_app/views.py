from django.shortcuts import render

from django.http import HttpResponse                    # imported
from . models import Blog                               # imported

# Create your views here.
def home(request):
    return render(request, 'index.html')

# def about(request):
#     return HttpResponse("This is About Page.")



def about(request):

    # fetch all the contents
    blogs = Blog.objects.all()                                            # similar sql --> # select * from blog

    return render(request, 'about.html', {'blogs' : blogs})               # render(request, template file, context)