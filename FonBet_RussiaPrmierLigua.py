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

ua = UserAgent(verify_ssl=False).chrome  
user_agent = ua
# user_agent = ua.random

print(f"\nuser_agent: {user_agent}\n")

driver = webdriver.Chrome('/home/petrucho/Downloads/chromedriver_linux64/chromedriver')

# Инициализация опций Chrome
chrome_options = Options()

# Добавление желаемых возможностей
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("user-agent=" + user_agent)

# Неявное ожидание
driver.implicitly_wait(10) # in seconds

# driver.get("https://www.lambdatest.com")

# Поиск элемента по ID
# email_form = driver.find_element_by_id("testing_form")

# Поиск элемента по XPath
# email_input = driver.find_element_by_xpath("//input[@name='email']")

# Поиск элемента по тегу
# email_input = driver.find_element_by_tag_name("input")

# Поиск элемента по тексту ссылки и частичному тексту ссылки
# email_input = driver.find_element_by_link_text('Start Free Testing')
# email_input = driver.find_element_by_partial_link_text('Start Free')

# driver.set_page_load_timeout(10)

# ФУТБОЛ РОССИЯ. ПРЕМЬЕР-ЛИГА
driver.get("https://www.fon.bet/sports/football/11935/")

# ЧМ 2022
# driver.get("https://www.fon.bet/football-2022/")


# wait until page will downloaded in browser
time.sleep(20)

# driver.get("https://www.ya.ru")
try:    
    page_source = driver.page_source
    print(page_source)

    # save screenshot of the page
    driver.save_screenshot('world_cup_2022.png')

    """
    xp_events_name = '//a[@class="table-component-text--5BmeJ sport-event__name--HefZL _clickable--G5cwQ _event-view--7J8rE _compact--7BwYe"]'
    xp_events_date = '//span[@class="event-block-planned-time__time--16Vaw _small--7aWII"]'
    xp_events_value = '//div[@class="table-component-factor-value_single--6nfox _compact--7j5yE"]'
    
    events_name = driver.find_elements(By.XPATH, xp_events_name)
    events_date = driver.find_elements(By.XPATH, xp_events_date)
    events_value = driver.find_elements(By.XPATH, xp_events_value)
    
    events_name_list = [value.text for value in events_name]
    events_date_list = [value.text for value in events_date]
    events_value_list = [value.text for value in events_value]

    print(f'\nevents_name_list: {events_name_list}\n')
    print(f'\nevents_date_list: {events_date_list}\n')
    print(f'\nevents_value_list: {events_value_list}\n')
    """
    
except:
    print("some error happen !!")
  