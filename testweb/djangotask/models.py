from django.db import models


class SiteUser(models.Model):
    # TODO: реализовать модель для взаимодействия с таблицей site_users
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    def get_name(self):
        return f'{self.last_name} {self.first_name}'

    class Meta:
        db_table = "site_users"


class Vacancy(models.Model):
    # TODO: реализовать модель для взаимодействия с таблицей vacancies
    name = models.TextField()
    salary = models.FloatField()
    area_name = models.TextField()
    published_at = models.TextField()

    class Meta:
        db_table = "vacancies"
