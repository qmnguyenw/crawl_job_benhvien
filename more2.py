from logging import error, exception
import os 
import base64
import json
import pprint
import time
import requests
import os.path

import selenium
from selenium import webdriver
from selenium.webdriver.common import desired_capabilities
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from bs4 import BeautifulSoup
import urllib.request
import urllib.parse
from urllib.request import urlopen, Request
from fake_useragent import UserAgent

capabilities = DesiredCapabilities.CHROME
capabilities['pageLoadStrategy'] = 'none'

# user_agent = UserAgent().random
user_agent = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
# Set profile folder
options = webdriver.ChromeOptions()
options.add_argument('--incognito')
options.add_argument(f'user-agent={user_agent}')

# Start driver
driver = webdriver.Chrome('E:/VM/ShareFolder/Working/web-crawl/crawl/chromedriver.exe', options=options, desired_capabilities=capabilities)

base_path = 'E:/VM/ShareFolder/Working/web-crawl/crawl/img/'

url = 'http://benhvienchinhhinh.net/kien-thuc-chuyen-mon/viem-xuong-chan-thuong.html'

driver.get(url)
time.sleep(3)

soup = BeautifulSoup(driver.page_source, 'html.parser')

article_slug = url.split('/')[-1]

os.mkdir(base_path + article_slug.split('.')[0])

for link in soup.select("img"):
    lnk = link['src']
    if ' ' in link['src']:
        lnk = urllib.parse.quote(link['src'], safe=':/')
    elif 'upload' in link['src']:
        lnk = 'http://benhvienchinhhinh.net' + link['src']
    else:
        lnk = link['src']

    try:
        img_path = base_path + article_slug.split('.')[0] + '/' + lnk.split('/')[-1]
        with open(img_path,'wb+') as f:
            # f.write(requests.get(lnk).content)
            try:
                req = Request(url=lnk, headers=headers) 
                html = urlopen(req).read()
                f.write(html)
            except:
                print(lnk)
    except Exception as err:
        print(err)

driver.close()