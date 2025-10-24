from django.db import models


# Create your models here.


# ---------------mod-19 || live-1-----------------
# 40:00


class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Course(models.Model):
    title = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)                     # one to many relationship [1 Department can has multiple course]

    def __str__(self):
        return self.title





# ---------------mod-19 || live-1-----------------


class Student(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    age = models.IntegerField()

    course = models.ManyToManyField(Course, null=True, blank=True, default=None)                              # many to many relationship [many students can have the same course also same students can take multiple course]

    photo = models.ImageField(upload_to='media/', null=True, blank=True, default=None)                                # after uploading an image it will be uploaded nad saved into "media" folder

    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True, blank=True, default=None)


    def __str__(self):
        return self.name
