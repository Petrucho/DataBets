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

    xp_block = '//div[@class="cup__table--6mj4v"]'
    # xp_team_name = '//span[@class="cup__team-name--MK92e"]'
    # xp_events_date = '//div[@class="cup__col--1j2cg _type_group--a0R16"]'
    # xp_events_value = '//span[@class="cup__factor-value--2zKDu"]'
    
    block_name = driver.find_elements(By.XPATH, xp_block)
    # team_name = driver.find_elements(By.XPATH, xp_team_name)
    # events_date = driver.find_elements(By.XPATH, xp_events_date)
    # events_value = driver.find_elements(By.XPATH, xp_events_value)
    
    block_name_list = [value.text for value in block_name]
    # team_name_list = [value.text for value in team_name]
    # events_date_list = [value.text for value in events_date]
    # events_value_list = [value.text for value in events_value]

    print(f'\nblock_name_list: {block_name_list}\n')
    # print(f'\nteam_name_list: {team_name_list}\n')
    # print(f'\nevents_date_list: {events_date_list}\n')
    # print(f'\nevents_value_list: {events_value_list}\n')
    
except:
    print("some error happen !!")



"""
block_name_list: ['20 ноября\nПобеда 1\nНичья\nПобеда 2\n19:00\nГруппа A\nКатар\n- : -\nЭквадор\n3.70\n3.25\n2.12\n+883', '21 ноября\nПобеда 1\nНичья\nПобеда 2\n16:00\nГруппа B\nАнглия\n- : -\nИран\n1.30\n4.90\n12.50\n+843\n19:00\nГруппа A\nСенегал\n- : -\nНидерланды\n5.60\n3.65\n1.68\n+888\n22:00\nГруппа B\nСША\n- : -\nУэльс\n2.60\n3.05\n3.00\n+883', '22 ноября\nПобеда 1\nНичья\nПобеда 2\n13:00\nГруппа C\nАргентина\n- : -\nСаудовская Аравия\n1.16\n7.30\n21.00\n+847\n16:00\nГруппа D\nДания\n- : -\nТунис\n1.42\n4.40\n8.50\n+853\n19:00\nГруппа C\nМексика\n- : -\nПольша\n2.75\n3.15\n2.75\n+886\n22:00\nГруппа D\nФранция\n- : -\nАвстралия\n1.22\n6.30\n15.00\n+860', '23 ноября\nПобеда 1\nНичья\nПобеда 2\n13:00\nГруппа F\nМарокко\n- : -\nХорватия\n4.70\n3.30\n1.88\n+888\n16:00\nГруппа E\nГермания\n- : -\nЯпония\n1.43\n4.70\n7.50\n+867\n19:00\nГруппа E\nИспания\n- : -\nКоста-Рика\n1.20\n6.30\n17.00\n+846\n22:00\nГруппа F\nБельгия\n- : -\nКанада\n1.35\n5.00\n9.00\n+857', '24 ноября\nПобеда 1\nНичья\nПобеда 2\n13:00\nГруппа G\nШвейцария\n- : -\nКамерун\n1.73\n3.50\n5.40\n+879\n16:00\nГруппа H\nУругвай\n- : -\nЮжная Корея\n1.75\n3.50\n5.20\n+885\n19:00\nГруппа H\nПортугалия\n- : -\nГана\n1.42\n4.30\n9.00\n+854\n22:00\nГруппа G\nБразилия\n- : -\nСербия\n1.45\n4.50\n7.60\n+863', '25 ноября\nПобеда 1\nНичья\nПобеда 2\n13:00\nГруппа B\nУэльс\n- : -\nИран\n2.25\n3.05\n3.70\n+882\n16:00\nГруппа A\nКатар\n- : -\nСенегал\n3.90\n3.15\n2.10\n+885\n19:00\nГруппа A\nНидерланды\n- : -\nЭквадор\n1.63\n4.00\n5.40\n+899\n22:00\nГруппа B\nАнглия\n- : -\nСША\n1.65\n3.90\n5.50\n+890', '26 ноября\nПобеда 1\nНичья\nПобеда 2\n13:00\nГруппа D\nТунис\n- : -\nАвстралия\n2.85\n3.00\n2.75\n+881\n16:00\nГруппа C\nПольша\n- : -\nСаудовская Аравия\n1.63\n3.85\n5.70\n+890\n19:00\nГруппа D\nФранция\n- : -\nДания\n2.00\n3.35\n4.00\n+890\n22:00\nГруппа C\nАргентина\n- : -\nМексика\n1.57\n3.90\n6.40\n+882', '27 ноября\nПобеда 1\nНичья\nПобеда 2\n13:00\nГруппа E\nЯпония\n- : -\nКоста-Рика\n1.85\n3.35\n4.70\n+889\n16:00\nГруппа F\nБельгия\n- : -\nМарокко\n1.52\n4.20\n6.50\n+896\n19:00\nГруппа F\nХорватия\n- : -\nКанада\n1.77\n3.80\n4.60\n+891\n22:00\nГруппа E\nИспания\n- : -\nГермания\n2.55\n3.35\n2.80\n+900', '28 ноября\nПобеда 1\nНичья\nПобеда 2\n13:00\nГруппа G\nКамерун\n- : -\nСербия\n4.40\n3.40\n1.90\n+885\n16:00\nГруппа H\nЮжная Корея\n- : -\nГана\n2.70\n2.95\n2.95\n+878\n19:00\nГруппа G\nБразилия\n- : -\nШвейцария\n1.50\n4.20\n7.20\n+894\n22:00\nГруппа H\nПортугалия\n- : -\nУругвай\n2.08\n3.35\n3.70\n+890', '29 ноября\nПобеда 1\nНичья\nПобеда 2\n18:00\nГруппа A\nЭквадор\n- : -\nСенегал\n2.95\n3.20\n2.55\n+888\n18:00\nГруппа A\nНидерланды\n- : -\nКатар\n1.32\n5.20\n10.00\n+861\n22:00\nГруппа B\nУэльс\n- : -\nАнглия\n6.10\n4.00\n1.58\n+888\n22:00\nГруппа B\nИран\n- : -\nСША\n3.45\n3.35\n2.15\n+894', '30 ноября\nПобеда 1\nНичья\nПобеда 2\n18:00\nГруппа D\nАвстралия\n- : -\nДания\n6.70\n3.70\n1.60\n+869\n18:00\nГруппа D\nТунис\n- : -\nФранция\n14.00\n5.60\n1.25\n+837\n22:00\nГруппа C\nПольша\n- : -\nАргентина\n5.00\n4.00\n1.68\n+888\n22:00\nГруппа C\nСаудовская Аравия\n- : -\nМексика\n6.40\n4.15\n1.55\n+887', '1 декабря\nПобеда 1\nНичья\nПобеда 2\n18:00\nГруппа F\nКанада\n- : -\nМарокко\n3.25\n3.30\n2.30\n+888\n18:00\nГруппа F\nХорватия\n- : -\nБельгия\n3.95\n3.65\n1.90\n+896\n22:00\nГруппа E\nКоста-Рика\n- : -\nГермания\n10.50\n5.30\n1.30\n+859\n22:00\nГруппа E\nЯпония\n- : -\nИспания\n10.00\n5.40\n1.30\n+866', '2 декабря\nПобеда 1\nНичья\nПобеда 2\n18:00\nГруппа H\nГана\n- : -\nУругвай\n4.80\n3.60\n1.78\n+887\n18:00\nГруппа H\nЮжная Корея\n- : -\nПортугалия\n9.00\n4.70\n1.38\n+855\n22:00\nГруппа G\nКамерун\n- : -\nБразилия\n9.50\n5.20\n1.35\n+856\n22:00\nГруппа G\nСербия\n- : -\nШвейцария\n2.80\n3.45\n2.50\n+893']
"""