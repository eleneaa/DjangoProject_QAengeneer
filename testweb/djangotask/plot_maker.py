import pandas as pd
import matplotlib.pyplot as plt


def allocation_vacancies(vacancies: pd.DataFrame):
    vac_cities = {"area_name": [], 'count_vac': []}
    for i in range(len(vacancies)):
        if vacancies.loc[i, 'area_name'] not in vac_cities["area_name"]:
            vac_cities['area_name'].append(vacancies.loc[i, 'area_name'])
            vac_cities['count_vac'].append(1)
        else:
            idx = vac_cities['area_name'].index(vacancies.loc[i, 'area_name'])
            vac_cities['count_vac'][idx] += 1

    vac_cities_df = pd.DataFrame(vac_cities)
    vac_cities_df = vac_cities_df.sort_values(by=['count_vac'])

    sum_vac = vac_cities_df['count_vac'].sum()
    vac_cities_df = vac_cities_df[vac_cities_df.count_vac > sum_vac * 0.01]

    plt.barh(vac_cities_df['area_name'], vac_cities_df['count_vac'])
    plt.show()

def year_vacancies(vacancies: pd.DataFrame):
    vac_year = {'year': [], 'count': []}
    for i in range(len(vacancies)):
        year = vacancies.loc[i, 'published_at'].split("T")[0][:4]
        if year not in vac_year['year']:
            vac_year['year'].append(year)
            vac_year['count'].append(1)
        else:
            idx = vac_year['year'].index(year)
            vac_year['count'][idx] += 1

    vac_year_df = pd.DataFrame(vac_year).sort_values(by=['year'])
    plt.bar(vac_year_df['year'], vac_year_df['count'])
    plt.show()

def top_skills(vacancies: pd.DataFrame):
    top_skills_pre = {}
    for i in range(len(vacancies)):
        year = vacancies.loc[i, 'published_at'].split("T")[0][:4]
        if isinstance(vacancies.loc[i, 'key_skills'], str):
            if year not in top_skills_pre.keys():
                top_skills_pre[year] = vacancies.loc[i, 'key_skills'].split("\n")
            else:
                skills = vacancies.loc[i, 'key_skills'].replace('\n', ', ').split(', ')
                top_skills_pre[year] = top_skills_pre[year]+skills

    top_skills = {}
    for year in top_skills_pre:
        top_skills[year] = {'skill': [], 'count': []}
        for skill in top_skills_pre[year]:
            if skill not in top_skills[year]['skill']:
                top_skills[year]['skill'].append(skill)
                top_skills[year]['count'].append(1)
            else:
                idx = top_skills[year]['skill'].index(skill)
                top_skills[year]['count'][idx] += 1
        skill_df = pd.DataFrame(top_skills[year]).sort_values(by=['count'], ascending=False).iloc[0:21]
        plt.barh(skill_df['skill'], skill_df['count'])
        plt.title(f'Топ-20 навыков за {year} год')
        plt.show()




    #print(top_skills)




if __name__ == '__main__':
    vacancies = pd.read_csv('vacancies.csv', encoding='utf-8', on_bad_lines='warn')
    #allocation_vacancies(vacancies)
    #year_vacancies(vacancies)
    top_skills(vacancies)

