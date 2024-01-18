from collections import Counter, OrderedDict
from math import floor
from operator import itemgetter

import pandas as pd
import requests

vacancies = pd.read_csv('vacancies.csv', encoding='utf-8', on_bad_lines='warn')


def df_filter_by_key(df_sorted: pd.DataFrame, key: str, column: str):
    list_cols = df_sorted.columns.tolist()
    list_rows = df_sorted.values
    key_index = list_cols.index(column)
    skills_index = list_cols.index('key_skills')
    value_list = []
    for row in list_rows:
        if key.lower() in str(row[key_index]).lower():
            value_list.append(row)
    return pd.DataFrame(data=value_list, columns=list_cols)


def normalize_skills(df: pd.DataFrame):
    df['key_skills'] = df['key_skills'].str.replace('\n', ' ')
    return df


def currency_to_RUR(df: pd.DataFrame):
    response = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
    currency = response.json()
    mask = df['salary_currency'] == 'RUR'
    df.loc[mask, 'salary_from'] = df.loc[mask, 'salary_from'] * float(currency["Valute"][df.loc[i, 'salary_currency']]['Value'])

df_filter_by_key(normalize_skills(vacancies), 'Тестировщик', 'name').to_csv(r'QAengineer.csv', index= False)
df_filter_by_key(normalize_skills(vacancies), 'QA', 'name').to_csv(r'QAengineer.csv', index= False)
