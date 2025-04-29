# news/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Башкы бет
    path('', views.news_list, name='news_list'),  # Бардык жаңылыктар
    path('<int:id>/', views.news_detail, name='news_detail'),   #Ар бир жаңылык үчүн
]
