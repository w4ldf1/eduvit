from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone


class News(models.Model):
    title = models.CharField("Название", max_length=200)
    content = models.TextField("Содержание")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="news")
    publication_date = models.DateTimeField("Дата публикации", default=timezone.now)
    image = models.URLField("Изображение", blank=True)

    class Meta:
        ordering = ["-publication_date"]
        verbose_name = "Новость"
        verbose_name_plural = "Новости"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("news_detail", kwargs={"pk": self.pk})


class Comment(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    text = models.TextField("Комментарий")
    created_at = models.DateTimeField("Дата создания", auto_now_add=True)
    updated_at = models.DateTimeField("Дата обновления", auto_now=True)
    is_published = models.BooleanField("Опубликован", default=True)

    class Meta:
        ordering = ["created_at"]
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"

    def __str__(self):
        return f"{self.user.username}: {self.text[:40]}"
