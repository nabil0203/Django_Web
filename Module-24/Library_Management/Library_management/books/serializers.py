from rest_framework import serializers
from . import models


# same as the form.py

class AuthorSerializer(serializers.ModelSerializer):
    books = serializers.StringRelatedField(many=True, read_only = True)                                   # Serializer relation -> Live_Class-1__24.12
    class Meta:
        model = models.Author
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    class Meta:

        model = models.Book
        fields = '__all__'
