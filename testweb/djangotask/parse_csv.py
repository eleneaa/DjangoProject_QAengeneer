import time
from collections import Counter, OrderedDict
from math import floor
from operator import itemgetter
import os
import pandas as pd
from cbrf.models import CurrenciesInfo, DailyCurrenciesRates, DynamicCurrenciesRates
from datetime import datetime
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

def convert_current(df: pd.DataFrame):
    for i in range(len(df)):
        if df.loc[i, 'salary_currency'] != "RUR":
            time.sleep(1)
            value = search_value(df.loc[i, 'published_at'], df.loc[i, 'salary_currency'])
            if df.loc[i, 'salary_to'] != '' and value is not None:
                df.loc[i, 'salary_to'] = float(df.loc[i, 'salary_to']) * float(value)
            if df.loc[i, 'salary_from'] != '' and search_value(df.loc[i, 'published_at'],
                                                             df.loc[i, 'salary_currency']) is not None:
                df.loc[i, 'salary_from'] = float(df.loc[i, 'salary_from']) * float(
                    search_value(df.loc[i, 'published_at'], df.loc[i, 'salary_currency']))
    return df


def search_value(date: str, char_code: str):
    date = date.split('T')
    date1 = date[0].split('-')
    c_info = CurrenciesInfo()
    var = c_info.currencies
    for cur in var.values():
        if cur.iso_char_code == char_code:
            dynamic_rates = DynamicCurrenciesRates(datetime(int(date1[0]), int(date1[1]), int(date1[2])), datetime(int(date1[0]), int(date1[1]), int(date1[2])), cur.id)
            if dynamic_rates.get_by_date(datetime(int(date1[0]), int(date1[1]), int(date1[2]))) is not None:
                return dynamic_rates.get_by_date(datetime(int(date1[0]), int(date1[1]), int(date1[2]))).value


filter_df = convert_current(normalize_skills(vacancies))
df_filter_by_key(filter_df, 'Тестировщик', 'name').to_csv(r'QAengineer.csv', index= False)
df_filter_by_key(filter_df, 'QA', 'name').to_csv(r'QAengineer.csv', index= False)
