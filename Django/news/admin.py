from django.contrib import admin

from .models import Comment, News


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "publication_date")
    list_filter = ("publication_date", "author")
    search_fields = ("title", "content")


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("news", "user", "created_at", "is_published")
    list_filter = ("is_published", "created_at")
    search_fields = ("text", "user__username", "news__title")
