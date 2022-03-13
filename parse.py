#!/home/bogdan/parse/venv/bin/python
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import os

def get_html():
    url = 'https://bank.gov.ua/ua/markets/exchangerates'
    r = requests.get(url)
    return r.text


def get_dollar(html):
    soup = BeautifulSoup(html, 'lxml')
    t = soup.find('td', text='USD').find_parent('tr').find_all('td')[-1].text
    return t

def message(msg):
    title = 'Долар США'
    os.system('notify-send "{}" "{}"'.format(title, msg))
    #print(f'{title}, {msg}')



def main():
    rate = get_dollar(get_html())
    message(rate)


if __name__ == '__main__':
    main()
