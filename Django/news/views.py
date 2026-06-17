from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

from .forms import CommentForm, NewsForm, RegisterForm
from .models import News


def staff_required(user):
    return user.is_staff or user.is_superuser


def home(request):
    latest_news = News.objects.select_related("author")[:3]
    return render(request, "news/home.html", {"latest_news": latest_news})


def contacts(request):
    return render(request, "news/contacts.html")


def news_list(request):
    query = request.GET.get("q", "").strip()
    sort = request.GET.get("sort", "new")
    news = News.objects.select_related("author")

    if query:
        news = news.filter(Q(title__icontains=query) | Q(content__icontains=query))

    if sort == "old":
        news = news.order_by("publication_date")
    else:
        news = news.order_by("-publication_date")

    context = {
        "news": news,
        "query": query,
        "sort": sort,
    }
    return render(request, "news/news_list.html", context)


def news_detail(request, pk):
    news_item = get_object_or_404(News.objects.select_related("author"), pk=pk)
    comments = news_item.comments.filter(is_published=True).select_related("user")

    if request.method == "POST":
        if not request.user.is_authenticated:
            return redirect("login")

        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.news = news_item
            comment.user = request.user
            comment.save()
            messages.success(request, "Комментарий добавлен")
            return redirect("news_detail", pk=news_item.pk)
    else:
        form = CommentForm()

    return render(request, "news/news_detail.html", {"news_item": news_item, "comments": comments, "form": form})


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Регистрация выполнена")
            return redirect("home")
    else:
        form = RegisterForm()

    return render(request, "registration/register.html", {"form": form})


@login_required
def profile(request):
    comments = request.user.comments.select_related("news").order_by("-created_at")
    return render(request, "news/profile.html", {"comments": comments})


@login_required
def password_change(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)

        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, "Пароль изменен")
            return redirect("profile")
    else:
        form = PasswordChangeForm(request.user)

    return render(request, "registration/password_change.html", {"form": form})


@user_passes_test(staff_required)
def news_create(request):
    if request.method == "POST":
        form = NewsForm(request.POST)

        if form.is_valid():
            news_item = form.save(commit=False)
            news_item.author = request.user
            news_item.save()
            messages.success(request, "Новость создана")
            return redirect("news_detail", pk=news_item.pk)
    else:
        form = NewsForm()

    return render(request, "news/news_form.html", {"form": form, "title": "Создание новости"})


@user_passes_test(staff_required)
def news_update(request, pk):
    news_item = get_object_or_404(News, pk=pk)

    if request.method == "POST":
        form = NewsForm(request.POST, instance=news_item)

        if form.is_valid():
            form.save()
            messages.success(request, "Новость обновлена")
            return redirect("news_detail", pk=news_item.pk)
    else:
        form = NewsForm(instance=news_item)

    return render(request, "news/news_form.html", {"form": form, "title": "Редактирование новости"})


@user_passes_test(staff_required)
def news_delete(request, pk):
    news_item = get_object_or_404(News, pk=pk)

    if request.method == "POST":
        news_item.delete()
        messages.success(request, "Новость удалена")
        return redirect("news_list")

    return render(request, "news/news_confirm_delete.html", {"news_item": news_item})
