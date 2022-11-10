# Импорт опций Chrome
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

import time

import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

from fake_useragent import UserAgent

# import split_div_TennisiBet
import save_to_csv

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

# ЧМ 2022
driver.get("https://tennisi.bet/?utm_source=bets-sites&utm_campaign=betonmobile_rating_betonmob_native-news_0_a7273&utm_medium=cpe")

# wait until page will downloaded in browser
time.sleep(20)

try:    
    # page_source = driver.page_source
    # print(f'page_source: {page_source}')

    # save screenshot of the page
    driver.save_screenshot('TennisiBet_world_cup_2022.png')

    # xp_block = '/html/body/table[1]'
    xp_block = '//table[@style="border-collapse: collapse; border-right-width:0;  border-top-width:0; border-left-width:0; border-bottom-width:0" cellspacing="0" cellpadding="0" bgcolor="white" border="1"]'
    block_name = driver.find_elements(By.XPATH, xp_block)    
    block_name_list = [value.text for value in block_name]
    print(f'\nblock_name_list: {block_name_list}\n')

    # splitted_list = split_div_TennisiBet.split_list(block_name_list) # split List
    # save_to_csv.save_to_file(splitted_list, 'TennisiBet') # splitted List saving to csv-file
    
except:
    print("some error happen !!")

