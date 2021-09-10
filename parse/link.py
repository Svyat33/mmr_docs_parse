import base64
import re

import requests
from bs4 import BeautifulSoup
from pydantic import HttpUrl

from parse.struct import Document, ExtensionsEnum


class DecisionLink:
    '''Итератор возвращает ссылку на решение исполкома'''

    def __init__(self, limit=10):
        self.__limit = limit
        self.__start = 0
        self.ses = requests.Session()

    @property
    def link(self):
        return f'https://mkrada.gov.ua/documents/?c=1&start={self.__start}'

    def __iter__(self):
        self.__start = 0
        self.__links = None
        self.__decision_idx = None
        return self

    def __load(self):
        ''' Загружает текущую ссылку и заполняет список решений из загруженной страницы в атрибут self.__links'''
        page = self.ses.get(self.link)
        self.__start += 10
        if not page.ok:
            raise ConnectionError
        tekpage = BeautifulSoup(page.text, 'lxml')
        divs = tekpage.find('main').find_all('div', class_='news_line_item')
        self.__links = ['https://mkrada.gov.ua' + a.find('a').attrs.get('href')
                        for a in divs
                        if a.find('a') and a.find('a').attrs.get('href')]

        self.__decision_idx = -1

    def __next__(self) -> HttpUrl:
        if self.__limit <= 0:
            raise StopIteration
        self.__limit -= 1
        if not self.__links:
            try:
                self.__load()
            except ConnectionError:
                raise StopIteration

        if not self.__links:
            raise StopIteration

        self.__decision_idx += 1
        return_link = self.__links[self.__decision_idx]
        if self.__decision_idx >= len(self.__links):
            self.__links = None
        return return_link


def get_one_decision(link: HttpUrl) -> Document:
    '''Извлечь решение по ссылке.'''
    page = requests.get(link)
    if not page.ok:
        raise ConnectionError
    page.encoding = 'utf-8'
    soup = BeautifulSoup(page.text, 'lxml')
    content = re.sub("\\xa0", ' ', soup.find('div', id='overcontent').text)
    title = '' + soup.find('span', class_='breadcrumbs__current').text
    return Document(
        title=title,
        link=link,
        file_content=base64.b64encode(content.encode()),
        file_type=ExtensionsEnum.txt
    )
