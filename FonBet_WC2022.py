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
    # driver.save_screenshot('world_cup_2022.png')
    
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
  