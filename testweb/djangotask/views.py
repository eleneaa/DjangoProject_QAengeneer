import json

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404

from .models import *

@csrf_exempt
def info(request):
    # TODO: вывести информацию о профессии
    return render(request, 'info.html')


def skills(request):
    # TODO: вывести перечень приоритетных скиллов для данной вакансии
    return render(request, 'base_template.html')


def recent_vacancies(request):
    # TODO: вывести список последних вакансий из апи hh.ru

    return render(request, 'base_template.html')


def geography(request):
    # TODO: вывести статистику по городам для вакансий
    return render(request, 'base_template.html')


def relevance(request):
    # TODO: ???
    return render(request, 'base_template.html')


