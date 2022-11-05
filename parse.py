import requests
from bs4 import BeautifulSoup as bs
import pandas as pd



# ФУТБОЛ РОССИЯ. ПРЕМЬЕР-ЛИГА
URL_TEMPLATE = "https://www.fon.bet/sports/football/11935/"

headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'        
      }
r = requests.get(URL_TEMPLATE, headers = headers)
print(r.status_code)
print(r.text)

# FILE_NAME = "test.csv"

"""
def parse(url = URL_TEMPLATE):
    result_list = {'href': [], 'title': [], 'about': []}
    r = requests.get(url)
    soup = bs(r.text, "html.parser")
    vacancies_names = soup.find_all('h2', class_='add-bottom-sm')
    vacancies_info = soup.find_all('p', class_='overflow')
    for name in vacancies_names:
        result_list['href'].append('https://www.work.ua'+name.a['href'])
        result_list['title'].append(name.a['title'])
    for info in vacancies_info:
        result_list['about'].append(info.text)
    return result_list


df = pd.DataFrame(data=parse())
df.to_csv(FILE_NAME)
"""