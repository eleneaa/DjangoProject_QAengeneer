from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.info, name='info'), #info
    path('recent_vacancies/', views.recent_vacancies, name='recent_vacancies'),
    path('skills/', views.skills, name='skills'),
    path('geography/', views.geography, name='geography'),
    path('relevance/', views.relevance, name='relevance')
]
