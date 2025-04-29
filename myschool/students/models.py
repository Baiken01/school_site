from django.db import models

class Gallery(models.Model):
    title = models.CharField(max_length=200, verbose_name="Аталышы")
    category = models.CharField(max_length=100, verbose_name="Категориясы")
    year = models.IntegerField(verbose_name="Жылы")
    image = models.ImageField(upload_to='gallery/', verbose_name="Сүрөт")

    def __str__(self):
        return self.title


from django.db import models
from datetime import date

class Project(models.Model):
    title = models.CharField(max_length=255, verbose_name="Аталуусу")
    created_at = models.DateField(default=date.today, verbose_name="Кошулган датасы")
    pdf_file = models.FileField(upload_to='projects/', verbose_name="PDF файлы", blank=True, null=True)

    def __str__(self):
        return self.title

