
class Vacancy:
    def __init__(self, vacancy_payload: dict):
        self.vacancy_name = vacancy_payload['name']
        self.description = 'ПИЗДА'
        self.key_skills = 'ОЧКО'
        self.employer_name = vacancy_payload['employer']['name']
        self.salary_from = vacancy_payload['salary']['from']
        self.salary_to = vacancy_payload['salary']['to']
        self.area_name = vacancy_payload['area']['name']
        self.publish_date = vacancy_payload['published_at']
        self.raw = vacancy_payload


