
from django.shortcuts import render
def home(request):
    # Акыркы 6 жаңылыкты алуу
    latest_news = News.objects.order_by('-date')[:6]
    return render(request, 'students/index.html', {'latest_news': latest_news})


def news_list(request):
    all_news = News.objects.all()  # Бардык жаңылыктарды алуу
    return render(request, 'news/news_list.html', {'all_news': all_news})
# Ар бир жанылыкты толук көрсөтүүчү функция
def news_detail(request, id):
    news_item = get_object_or_404(News, id=id)  # Жанылыкты ID боюнча табабыз
    return render(request, 'news/news_detail.html', {'news_item': news_item})

from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import News  # News моделиң бул app ичинде экенин билебиз

def news_detail(request, id):
    news_item = get_object_or_404(News, pk=id)
    data = {
        'title': news_item.title,
        'date': news_item.created_at.strftime('%d.%m.%Y'),
        'content': news_item.content,
        'image_url': news_item.image.url if news_item.image else '',
    }
    return JsonResponse(data)
