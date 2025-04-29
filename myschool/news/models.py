from django.db import models
from django.utils import timezone

class News(models.Model):
    title = models.CharField("Аталышы", max_length=255)
    content = models.TextField("Толук маалымат")
    image = models.ImageField("Сүрөт", upload_to='news_images/', blank=True, null=True)
    created_at = models.DateTimeField("Кошулган убакыт", auto_now_add=True)
    date = models.DateField("Дата", default=timezone.now)  # Бул жерде дата да кошулду

    def __str__(self):
        return self.title
