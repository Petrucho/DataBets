import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# from fake_useragent import UserAgent
# UserAgent().chrome  
# UserAgent(verify_ssl=False).chrome  
# ua = UserAgent(verify_ssl=False)
# user_agent = ua.random

# print(f"\nUserAgent().chrome:\n{UserAgent().chrome}\n")
# print(f"\ntype(UserAgent().chrome):\n{type(UserAgent().chrome)}\n")

# ФУТБОЛ РОССИЯ. ПРЕМЬЕР-ЛИГА
# URL_TEMPLATE = "https://www.fon.bet/sports/football/11935/"
URL_TEMPLATE = 'https://clientsapi04w.bk6bba-resources.com/content/getContentById'

"""
curl = 'https://clientsapi04w.bk6bba-resources.com/content/getContentById' \    
  -H 'Accept: */*' \
  -H 'Accept-Language: en-US,en;q=0.8' \
  -H 'Cache-Control: no-cache' \
  -H 'Connection: keep-alive' \
  -H 'Content-Type: text/plain;charset=UTF-8' \
  -H 'Origin: https://www.fon.bet' \
  -H 'Pragma: no-cache' \
  -H 'Referer: https://www.fon.bet/' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Site: cross-site' \
  -H 'Sec-GPC: 1' \
  -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36' \
  --data-raw '{"id":"32678","lang":"ru","lastVersion":"0","scopeMarketId":"1600","sysId":1}' \
  --compressed
"""

headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.8',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Content-Length': '77',
        'Content-Type': 'text/plain;charset=UTF-8',        
        'Origin': 'https://www.fon.bet',
        'Pragma': 'no-cache',
        'Referer': 'https://www.fon.bet/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'cross-site',
        'Sec-GPC': '1',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'        
      }

# headers = {
#     'Accept': '*/*',
#     'User-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582'
# }

# headers = {
#     user_agent
# }


r = requests.get(URL_TEMPLATE, headers=headers, data-raw={"id":"32678","lang":"ru","lastVersion":"0","scopeMarketId":"1600","sysId":1})
print(f'r.status_code:\n{r.status_code}')
print(f'r.text:\n{r.text}')

# try to use logging
# logging.info(f"{user_name=} send message: {message.text}")

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