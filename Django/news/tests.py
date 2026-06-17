from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from .models import Comment, News


class NewsSiteTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="student", email="student@example.com", password="StrongPass123")
        self.staff = User.objects.create_user(
            username="manager",
            email="manager@example.com",
            password="StrongPass123",
            is_staff=True,
        )
        self.news = News.objects.create(
            title="Первая новость",
            content="Содержание первой новости",
            author=self.staff,
            publication_date=timezone.now(),
            image="https://example.com/image.jpg",
        )

    def test_news_model_string_and_url(self):
        self.assertEqual(str(self.news), "Первая новость")
        self.assertEqual(self.news.get_absolute_url(), reverse("news_detail", kwargs={"pk": self.news.pk}))

    def test_home_page_shows_latest_news(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Первая новость")

    def test_news_search_filters_by_title(self):
        News.objects.create(
            title="Вторая запись",
            content="Другой текст",
            author=self.staff,
            publication_date=timezone.now(),
        )
        response = self.client.get(reverse("news_list"), {"q": "Первая"})
        self.assertContains(response, "Первая новость")
        self.assertNotContains(response, "Вторая запись")

    def test_register_creates_user(self):
        response = self.client.post(
            reverse("register"),
            {
                "username": "newuser",
                "email": "newuser@example.com",
                "password1": "StrongPass123",
                "password2": "StrongPass123",
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertTrue(User.objects.filter(username="newuser").exists())

    def test_authenticated_user_can_add_comment(self):
        self.client.login(username="student", password="StrongPass123")
        response = self.client.post(reverse("news_detail", kwargs={"pk": self.news.pk}), {"text": "Хорошая новость"})
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Comment.objects.filter(news=self.news, user=self.user, text="Хорошая новость").exists())

    def test_anonymous_user_redirected_from_comment(self):
        response = self.client.post(reverse("news_detail", kwargs={"pk": self.news.pk}), {"text": "Текст"})
        self.assertEqual(response.status_code, 302)
        self.assertIn(reverse("login"), response["Location"])

    def test_staff_can_create_news(self):
        self.client.login(username="manager", password="StrongPass123")
        response = self.client.post(
            reverse("news_create"),
            {
                "title": "Созданная новость",
                "content": "Текст созданной новости",
                "image": "",
                "publication_date": "2026-01-01T12:00",
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertTrue(News.objects.filter(title="Созданная новость").exists())

    def test_regular_user_cannot_create_news(self):
        self.client.login(username="student", password="StrongPass123")
        response = self.client.get(reverse("news_create"))
        self.assertEqual(response.status_code, 302)
        self.assertIn(reverse("login"), response["Location"])
