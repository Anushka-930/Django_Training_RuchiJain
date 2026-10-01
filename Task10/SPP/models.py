from django.db import models

class Student(models.Model):
    student_id = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    course = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    cgpa = models.FloatField(null=True, blank=True)
    programming_skills = models.TextField(null=True, blank=True)
    technical_skills = models.TextField(null=True, blank=True)
    communication_skills = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name