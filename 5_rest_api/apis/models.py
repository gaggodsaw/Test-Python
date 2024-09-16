from django.db import models

class School(models.Model):
    name = models.CharField(max_length=255)
    abbreviation = models.CharField(max_length=50)
    address = models.TextField()

class Classroom(models.Model):
    school = models.ForeignKey(School, related_name='classrooms', on_delete=models.CASCADE)
    year = models.CharField(max_length=10)
    section = models.CharField(max_length=10)

class Teacher(models.Model):
    school = models.ForeignKey(School, related_name='teachers', on_delete=models.CASCADE)
    classrooms = models.ManyToManyField(Classroom, related_name='teachers')
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)

class Student(models.Model):
    classroom = models.ForeignKey(Classroom, related_name='students', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)