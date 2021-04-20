from bs4 import BeautifulSoup as BS
import requests
import re

from loguru import logger

from datetime import datetime


def _month_to_int(month: str):
    month = month.lower()
    if month=='января': return 1
    if month=='февраля': return 2
    if month=='марта': return 3
    if month=='апреля': return 4
    if month=='мая': return 5
    if month=='июня': return 6
    if month=='июля': return 7
    if month=='августа': return 8
    if month=='сентября': return 9
    if month=='октября': return 10
    if month=='ноября': return 11
    if month=='декабря': return 12
    
def to_datetime(date: str) -> datetime:
    if '/' in date:
        date = date.split('/')
        day, month, year = int(date[0]), int(date[1]), int('20'+date[2])

    else:
        date = date.split()
        day = int(date[0])
        month = int(_month_to_int(date[1]))
        year = int(date[2])

    hours = date[-1].split(':')
    if int(hours[0]) == int(date[2]): hours = [0, 0]

    response = datetime(year, month, day, int(hours[0]), int(hours[1]))
    return response

def extract_domain(url: str) -> str:
    return [re.search(r'https://.*?/', url)[0].split('/')[-2]][0]

def get_div(url, content, contentType):
    response = requests.get(url)
    soup = BS(response.text, 'html.parser')

    string = soup.find(string=content)
    divsTypes = ['a', 'span', 'div', 'br', 'h1', 'li', 'i', 'b', 'p']
    contTypes = ['comments', 'views', 'vote', 'bookmark']
    str_div = ''

    if string:
        pass
    else:
        logger.error('Not found such string as: ' + content)
        logger.error("  content type: " + contentType)
        return "Not found"

    for divType in divsTypes:

        logger.debug('now checking:' + divType)
        parents = string.find_parents(divType)
        

        if (len(parents) > 0):
            block = parents[0]
            str_block = str(block)

            count = 0
            for char in str_block:
                if (char == '<') or (char == '>'):
                    count += 1
                else: pass

            if (count == 4):
                logger.warning(str_block)
                if contentType in contTypes:
                    if contentType in str_block:
                        logger.info(str_block)
                        str_div = str_block
                else:
                    str_div = str_block
            else: pass

        else: pass

    return str_div

get_div('https://habr.com/ru/company/ruvds/blog/553068/', '4', 'comments')