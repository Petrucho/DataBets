# Импорт опций Chrome
from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService
# from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

from fake_useragent import UserAgent


user_agent = UserAgent(verify_ssl=False).chrome
# print(f"\nuser_agent: {user_agent}\n")

driver = webdriver.Chrome('/home/petrucho/Downloads/chromedriver_linux64/chromedriver')

# Инициализация опций Chrome
chrome_options = Options()

# Добавление желаемых возможностей
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("user-agent=" + user_agent)

# Неявное ожидание
driver.implicitly_wait(10) # in seconds

# driver.set_page_load_timeout(10)

# ЧМ 2022
driver.get("https://www.fon.bet/football-2022/")

# wait until page will downloaded in browser
time.sleep(10)

# driver.get("https://www.ya.ru")
try:    
    # page_source = driver.page_source
    # print(page_source)

    # save screenshot of the page
    driver.save_screenshot('world_cup_2022.png')
    
    xp_team_name = '//span[@class="cup__team-name--MK92e"]'
    xp_events_date = '//div[@class="cup__col--1j2cg _type_group--a0R16"]'
    xp_events_value = '//span[@class="cup__factor-value--2zKDu"]'
    
    team_name = driver.find_elements(By.XPATH, xp_team_name)
    events_date = driver.find_elements(By.XPATH, xp_events_date)
    events_value = driver.find_elements(By.XPATH, xp_events_value)
    
    team_name_list = [value.text for value in team_name]
    events_date_list = [value.text for value in events_date]
    events_value_list = [value.text for value in events_value]

    print(f'\nteam_name_list: {team_name_list}\n')
    print(f'\nevents_date_list: {events_date_list}\n')
    print(f'\nevents_value_list: {events_value_list}\n')    
    
except:
    print("some error happen !!")

"""
team_name_list = ['Катар', 'Эквадор', 'Англия', 'Иран', 'Сенегал', 'Нидерланды', 'США', 'Уэльс', 'Аргентина', 'Саудовская Аравия', 'Дания', 'Тунис', 'Мексика', 'Польша', 'Франция', 'Австралия', 'Марокко', 'Хорватия', 'Германия', 'Япония', 'Испания', 'Коста-Рика', 'Бельгия', 'Канада', 'Швейцария', 'Камерун', 'Уругвай', 'Южная Корея', 'Португалия', 'Гана', 'Бразилия', 'Сербия', 'Уэльс', 'Иран', 'Катар', 'Сенегал', 'Нидерланды', 'Эквадор', 'Англия', 'США', 'Тунис', 'Австралия', 'Польша', 'Саудовская Аравия', 'Франция', 'Дания', 'Аргентина', 'Мексика', 'Япония', 'Коста-Рика', 'Бельгия', 'Марокко', 'Хорватия', 'Канада', 'Испания', 'Германия', 'Камерун', 'Сербия', 'Южная Корея', 'Гана', 'Бразилия', 'Швейцария', 'Португалия', 'Уругвай', 'Эквадор', 'Сенегал', 'Нидерланды', 'Катар', 'Уэльс', 'Англия', 'Иран', 'США', 'Австралия', 'Дания', 'Тунис', 'Франция', 'Польша', 'Аргентина', 'Саудовская Аравия', 'Мексика', 'Канада', 'Марокко', 'Хорватия', 'Бельгия', 'Коста-Рика', 'Германия', 'Япония', 'Испания', 'Гана', 'Уругвай', 'Южная Корея', 'Португалия', 'Камерун', 'Бразилия', 'Сербия', 'Швейцария']
events_value_list = ['3.70', '3.30', '2.10', '1.30', '4.90', '12.50', '5.70', '3.70', '1.65', '2.50', '3.10', '3.10', '1.16', '7.30', '21.00', '1.40', '4.40', '9.00', '2.75', '3.20', '2.70', '1.22', '6.30', '15.00', '4.70', '3.30', '1.88', '1.45', '4.60', '7.30', '1.20', '6.30', '18.00', '1.37', '4.90', '9.00', '1.75', '3.50', '5.30', '1.75', '3.55', '5.20', '1.43', '4.30', '9.00', '1.45', '4.50', '7.70', '2.25', '3.05', '3.70', '4.10', '3.20', '2.03', '1.60', '4.10', '5.70', '1.65', '3.90', '5.50', '2.85', '3.00', '2.75', '1.63', '3.85', '5.70', '1.93', '3.45', '4.20', '1.57', '3.90', '6.40', '1.85', '3.35', '4.70', '1.52', '4.20', '6.50', '1.77', '3.80', '4.60', '2.45', '3.40', '2.95', '4.40', '3.40', '1.90', '2.70', '2.95', '2.95', '1.50', '4.15', '7.10', '2.02', '3.40', '3.85', '2.95', '3.20', '2.55', '1.32', '5.20', '10.00', '6.10', '4.00', '1.58', '3.45', '3.40', '2.17', '6.50', '3.75', '1.60', '14.00', '5.60', '1.25', '5.00', '4.00', '1.68', '6.40', '4.15', '1.55', '3.25', '3.30', '2.30', '3.95', '3.65', '1.90', '10.50', '5.30', '1.30', '10.00', '5.40', '1.30', '4.80', '3.60', '1.78', '9.00', '4.70', '1.38', '9.50', '5.20', '1.35', '2.80', '3.45', '2.50']

'Катар', 'Эквадор', 3.70', '3.30', '2.10'
'Англия', 'Иран', '1.30', '4.90', '12.50'
"""