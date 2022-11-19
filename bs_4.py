from bs4 import BeautifulSoup
import lxml
import requests

def link_downloads():
    url = 'https://pypi.org/project/beautifulsoup4/'
    response = requests.get(url=url)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')
    div = soup.find('h1', class_='package-header__name').text
    print(f'Текщая версия {div}')

