from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
]
from django.contrib import admin
from django.urls import path, include
from students import views as student_views  # <-- Мында students.views'ти кош


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', student_views.home, name='home'),  # Башкы бетке students/views.py'den home
    path('news/', include('news.urls')),  # Жаңылыктар үчүн news.urls
    path('about/', views.about, name='about'),
    path('struktura/', views.struktura, name='struktura'),
    path('success/', views.success, name='success'),
    path('knowledge', views.knowledge, name='knowledge'),
    path('parlament', views.parlament, name='parlament'),
    path('courses', views.courses, name='courses'),
    path('dekada', views.dekada, name='dekada'),
    path('pupils', views.pupils, name='pupils'),
    path('parents', views.parents, name='parents'),

    path('gallery/', views.gallery, name='gallery'),

path('project/', views.project_view, name='project'),

]


