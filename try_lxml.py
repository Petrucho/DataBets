from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup

try:
    html = urlopen("https://www.ya.ru/")
except HTTPError as e:
    print("The server returned an HTTP error:\n")
    print(e)
except URLError as e:
    print("The server could not be found!")
else:
    bs = BeautifulSoup(html.read(), 'html5lib')
    print(bs)