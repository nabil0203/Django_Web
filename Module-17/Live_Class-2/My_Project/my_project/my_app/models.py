from django.db import models

# Create your models here.

class Blog(models.Model):                            # Blog = Table name of SQL
    name = models.CharField(max_length=100)          # "name" is a Column
    content = models.TextField()                     # "content" is a column