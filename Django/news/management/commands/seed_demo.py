from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.utils import timezone

from news.models import Comment, News


class Command(BaseCommand):
    def handle(self, *args, **options):
        admin, created = User.objects.get_or_create(
            username="admin",
            defaults={
                "email": "admin@eduvit.local",
                "is_staff": True,
                "is_superuser": True,
            },
        )

        if created:
            admin.set_password("admin12345")
            admin.save()

        student, student_created = User.objects.get_or_create(
            username="student",
            defaults={
                "email": "student@eduvit.local",
            },
        )

        if student_created:
            student.set_password("student12345")
            student.save()

        demo_news = [
            {
                "title": "Открытие учебного семестра",
                "content": "В новом семестре студентов ждут проектные задания, практические занятия и консультации с преподавателями.",
                "image": "https://images.unsplash.com/photo-1523580846011-d3a5bc25702b?auto=format&fit=crop&w=1000&q=80",
            },
            {
                "title": "Неделя веб-разработки",
                "content": "Кафедра проводит серию встреч по Django, React и базам данных для студентов всех курсов.",
                "image": "https://images.unsplash.com/photo-1516321318423-f06f85e504b3?auto=format&fit=crop&w=1000&q=80",
            },
            {
                "title": "Конкурс студенческих проектов",
                "content": "Команды смогут представить свои учебные приложения и получить обратную связь от преподавателей.",
                "image": "https://images.unsplash.com/photo-1552664730-d307ca884978?auto=format&fit=crop&w=1000&q=80",
            },
            {
                "title": "Расписание консультаций",
                "content": "Консультации по программированию будут проходить каждую среду после основных занятий.",
                "image": "https://images.unsplash.com/photo-1497366754035-f200968a6e72?auto=format&fit=crop&w=1000&q=80",
            },
        ]

        for index, item in enumerate(demo_news):
            news_item, _ = News.objects.get_or_create(
                title=item["title"],
                defaults={
                    "content": item["content"],
                    "author": admin,
                    "image": item["image"],
                    "publication_date": timezone.now() - timezone.timedelta(days=index),
                },
            )
            Comment.objects.get_or_create(
                news=news_item,
                user=student,
                text="Полезная информация, спасибо за публикацию.",
            )

        self.stdout.write(self.style.SUCCESS("Демо-данные созданы"))
