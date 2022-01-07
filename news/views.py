from django.shortcuts import render
from news.models import News
from django.http import HttpResponse
from django.core.cache import cache



 # полная информация о новости
def news_detail(request, news_pk):
    news = News.objects.get(id=news_pk)
    return render(request, 'news_detail.html', {'news': news})


# главная страница приложения.
def index(request):
    news = News.objects.all()
    return render(request, "index.html", {"news": news})
