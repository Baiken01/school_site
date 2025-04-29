from django.db import models

class Teacher(models.Model):
    full_name = models.CharField(max_length=100)
    position = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='teacher_photos/')
    resume = models.FileField(upload_to='teacher_resumes/')

    def __str__(self):
        return self.full_name

