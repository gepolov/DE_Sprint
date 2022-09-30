import requests
import json

def getData():
    perpage = 100
    req = requests.get(f'https://api.hh.ru/vacancies?text=python+разработчик&area=113&per_page={perpage}').json()
    pages = int(req.get('found') / perpage)
    final = {}
    final['data'] = []

    for i in range(1):
        req = requests.get(f'https://api.hh.ru/vacancies?text=python+разработчик&area=113&per_page={perpage}&page={i}').json()
        try:
            for k in range(len(req.get('items'))):
                dic = {}
                title = req.get('items')[k].get('name')
                dic['title'] = title

                vacancy_id = req.get('items')[k].get('id')
                req_vacancy = requests.get(f'https://api.hh.ru/vacancies/{vacancy_id}').json()

                if 'experience' in req_vacancy:
                    experience = req_vacancy.get('experience').get('name')
                    dic['work experience'] = experience

                if 'salary' in req.get('items')[k] and req.get('items')[k].get('salary') is not None:
                    if req.get('items')[k].get('salary').get('from') is not None:
                        salary_min = req.get('items')[k].get('salary').get('from')
                    else:
                        salary_min = 0
                    if req.get('items')[k].get('salary').get('to') is not None:
                        salary_max = req.get('items')[k].get('salary').get('to')
                    else:
                        salary_max = 0
                    salary = max(salary_min, salary_max)
                    dic['salary'] = salary

                region = req.get('items')[k].get('area').get('name')
                dic['region'] = region
                final['data'].append(dic)

        except: pass
    print(final)
    print(len(final['data']))

    with open('data.json', 'w', encoding='utf-8', newline='') as outfile:
        json.dump(final, outfile, sort_keys = False, indent = 4, ensure_ascii = False, separators=(',', ': '))

getData()

