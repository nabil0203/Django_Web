from django.shortcuts import render

from django.http import HttpResponse                    # imported


# Create your views here.
def home(request):
    return render(request, 'index.html')

def about(request):
    return HttpResponse("This is About Page.")