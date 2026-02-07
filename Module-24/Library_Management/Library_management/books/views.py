from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer


# class based view
from rest_framework import viewsets




# -------------------- Function based View ----------------------------


# Author create

@api_view(['GET', 'POST'])                                                                  # this view will have both GET & POST request
def author_list_create(request):


    # get request
    if request.method == 'GET':
        authors = Author.objects.all()                                                      # this gives a query set --> List of Dictionary (Author list)
        serializer = AuthorSerializer(authors, many = True)                                 # (same as forms) as GET request, we are fetching data from DB as query set
                                                                                            # then converting the query set into --> JSON ; here, using serializer instead of forms

        return Response(serializer.data, status=status.HTTP_200_OK)                         # we will get the data from DB and HTTP 200 response



    # post request
    elif request.method == 'POST':
        serializer = AuthorSerializer(data=request.data)                                           #  as POST request we are creating data; here, instead of forms using serializer 

        if serializer.is_valid():                                                                   # if the serializer is valid, save and set status to 'Created' 
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED) 

        else:                                                                                       # if the serializer is not valid, return error and set status to 'bad request'
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)









# Book create
# same as the author create

@api_view(['GET', 'POST'])
def book_list_create(request):


    # get request
    if request.method == 'GET':
        book = Book.objects.all()
        serializer = BookSerializer(book, many = True)

        return Response(serializer.data, status=status.HTTP_200_OK)



    # post request
    elif request.method == 'POST':
        serializer = BookSerializer(data=request.data)

        if serializer.is_valid(): 
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED) 

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)






    


# -------------------- Class based View ----------------------------

# class handles 4 Request at a single time
# get, post, put/patch, delete
# check Live_class-2--->24.02





class AuthorViewSet(viewsets.ModelViewSet):

    queryset = Author.objects.all()
    serializer_class = AuthorSerializer





