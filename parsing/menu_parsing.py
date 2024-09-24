from urllib.request import urlopen
import logging 
import re #tìm các class trong HTML
from bs4 import BeautifulSoup

logger = logging.getLogger()

all_list = []

def menu_extract(link):
    html = urlopen(link)
    bs = BeautifulSoup(html, 'html.parser')
    # extract a list of category
    menu_list = bs.find_all('div', attrs={"class": re.compile('StyledItemV2')})

    for menu in menu_list:
        menu_item = menu.fill_all('a', href=True)
        all_list.append(menu_item[0]['href']) 
    return all_list
# print on when a build done seccessfully
logger.info('Starting to crawl...')