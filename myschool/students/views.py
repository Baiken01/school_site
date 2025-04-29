from news.models import News
from .models import Project
from django.shortcuts import render
from .models import Gallery

def homepage(request):
    return render(request, 'students/index.html')

def home(request):
    latest_news = News.objects.order_by('-created_at')  # туура версиясы
    return render(request, 'students/index.html', {'latest_news': latest_news})

def about(request):
    return render(request, 'students/about.html')  # about.html файлы students/templates/students/ ичинде болот

def struktura(request):
    return render(request, 'students/struktura.html')

def parlament(request):
    return render(request, 'students/parlament.html')

def courses(request):
    return render(request, 'students/courses.html')

def dekada(request):
    return render(request, 'students/dekada.html')

def success(request):
    return render(request, 'students/success.html')

def knowledge(request):
    return render(request, 'students/knowledge.html')

def pupils(request):
    return render(request, 'students/pupils.html')

def parents(request):
    return render(request, 'students/parents.html')



def gallery(request):
    gallery = Gallery.objects.all().order_by('-id')  # жаңы кошулган сүрөттөр биринчи чыгып туруш үчүн
    return render(request, 'students/gallery.html', {'gallery': gallery})


def project_view(request):
    projects = Project.objects.all()  # Бардык проекттерди базадан алабыз
    return render(request, 'students/project.html', {'projects': projects})



