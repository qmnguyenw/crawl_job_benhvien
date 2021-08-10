from logging import exception
import os 
import base64
import json
import pprint
import time

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
driver = webdriver.Chrome('./chromedriver.exe', options=options, desired_capabilities=capabilities)

url_list = list()

with open('./3-tintuc-link.txt', 'r') as f:
    for line in f:
        if line.strip() != '': url_list.append(line)

for link in url_list:
    driver.get(link)
    time.sleep(3)

    # soup = BeautifulSoup(driver.page_source, 'html.parser')
    slug = str(link).split('/')[5]
    item_title = driver.find_element_by_class_name('itemTitle')
    item_author = driver.find_element_by_class_name('itemAuthor')
    item_body = driver.find_element_by_class_name('itemBody')
    img = driver.find_elements_by_css_selector('img')
    txt = slug.strip() + '|' + item_title.text + '|' + item_author.text + '|' + repr(item_body.text) + '|' + ', '.join(i.get_attribute('src') for i in img) + '\n'
    with open(f'3-tintuc.csv', 'a', encoding='utf-8') as f:
        f.write(txt)

driver.close()
