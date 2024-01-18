import json
import urllib
from asyncio import sleep

import requests
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
#from .vacancies_class import Vacancy

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
    main_api = 'https://api.hh.ru/'
    vacancies_url = 'vacancies?'
    text = 'Тестировщик'
    per_page = 10
    url = main_api + vacancies_url + urllib.parse.urlencode({'text': text, 'per_page': per_page})
    json_data = requests.get(url).json().get('items')
    vacancies = []
    for vac in json_data:
        vac_obj = Vacancy(vac)
        vac_obj.set_description()
        sleep(1)
        vac_obj.set_key_skills()
        vacancies.append(vac_obj)

    return render(request, 'recent_vacancies.html', {'data': vacancies})


def geography(request):
    # TODO: вывести статистику по городам для вакансий
    payload = Plot.objects.filter(tag='g')
    return render(request, 'geography.html', {'plots': payload})


def relevance(request):
    # TODO: ???
    return render(request, 'base_template.html')


class Vacancy:
    def __init__(self, vacancy_payload: dict):
        self.description = None
        self.key_skills = None
        self.id = vacancy_payload['id']
        self.vacancy_name = vacancy_payload['name']
        self.employer_name = vacancy_payload['employer']['name']
        self.salary_from = vacancy_payload['salary']
        self.salary_to = vacancy_payload['salary']
        self.area_name = vacancy_payload['area']['name']
        self.publish_date = vacancy_payload['published_at']

    def get_info(self):
        return requests.get('https://api.hh.ru/vacancies/' + self.id).json()

    def set_description(self):
        # вот тут чистить от тегов штуку справа
        self.description = self.get_info().get('description')

    def set_key_skills(self):
        res = ''
        skills = self.get_info().get('key_skills')
        for s in skills:
            res += s['name'] + ', '
        self.key_skills = res[:-2]




