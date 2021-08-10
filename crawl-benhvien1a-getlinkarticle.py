from logging import exception
import os 
import os.path
import base64
import json
import pprint
import time
import requests

import selenium
from selenium import webdriver
from selenium.webdriver.common import desired_capabilities
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from bs4 import BeautifulSoup

capabilities = DesiredCapabilities.CHROME
capabilities['pageLoadStrategy'] = 'none'

# Set profile folder
options = webdriver.ChromeOptions()
options.add_argument('--incognito')

# Start driver
driver = webdriver.Chrome('E:/VM/ShareFolder/Working/web-crawl/crawl/chromedriver.exe', options=options, desired_capabilities=capabilities)
# driver = webdriver.Chrome('./chromedriver.exe', options=options, desired_capabilities=capabilities)

url_pagelist = set()

article_list = set()

for i in range(1,8):
    url_pagelist.add(f'http://benhvienchinhhinh.net/kien-thuc-chuyen-mon.html?page={i}')

# for i in range(1,5):
#     url_pagelist.add(f'http://benhvienchinhhinh.net/tin-moi-nhat.html?page={i}')

for url_link in url_pagelist:
    driver.get(url_link)
    time.sleep(3)

    soup = BeautifulSoup(driver.page_source, 'html.parser')

    article_div = soup.find_all('a', {'class': 'link'})
    
    for i in article_div:
        article_list.add(i['href'])

    print('Done', url_link)

with open(f'link_kienthuc.txt', 'w', encoding='utf-8') as f:
    for i in article_list:
        f.write(i+'\n')

print('Done!!!')
driver.close()
