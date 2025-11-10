from django.db import models


# Create your models here.


class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Course(models.Model):
    title = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.title




class Student(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    age = models.IntegerField()

    course = models.ManyToManyField(Course, null=True, blank=True, default=None)

    photo = models.ImageField(upload_to='media/', null=True, blank=True, default=None)

    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True, blank=True, default=None)


    def __str__(self):
        return self.name
