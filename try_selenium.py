# Импорт опций Chrome
from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService
# from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from fake_useragent import UserAgent

ua = UserAgent(verify_ssl=False)
user_agent = ua.random

print("\nUSER AGENT: " + user_agent)

driver = webdriver.Chrome('/home/petrucho/Downloads/chromedriver_linux64/chromedriver')

# Инициализация опций Chrome
chrome_options = Options()

# Добавление желаемых возможностей
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("user-agent=" + user_agent)

# Неявное ожидание
# driver.implicitly_wait(10) # in seconds

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

# ФУТБОЛ РОССИЯ. ПРЕМЬЕР-ЛИГА
driver.get("https://www.fon.bet/sports/football/11935/")
try:
    all_cookies = driver.get_cookies()
    for cookie_name, cookie_value in all_cookies.items():
        print("%s -> %s", cookie_name, cookie_value)

    # element = WebDriverWait(driver, 10).until(
    #     EC.presence_of_all_elements_located((By.ID, "testing_form"))
    )
except:
    print("some error happen !!")