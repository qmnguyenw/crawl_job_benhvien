from logging import error, exception
import os 
import base64
import json
import pprint
import time
import requests
import os.path

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
import htmlmin

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
# driver = webdriver.Chrome('E:/VM/ShareFolder/Working/web-crawl/crawl/chromedriver.exe', options=options, desired_capabilities=capabilities)
driver = webdriver.Chrome('/home/quang/Downloads/chromedriver', options=options, desired_capabilities=capabilities)

base_path = './total-tintuc/'

article_list = set()

with open('./link_tintuc.txt', 'r') as f:
    for line in f:
        if line.strip() != '': article_list.add(line)

loop = 0

ignore_img_list = [
    'footer-logo.png',
    'icon-back-to-top.png',
    'logo_1397577072.png',
    'logo_new.png',
    'logo-benh-vien.png',
    'logo-benh-vien-mobile-white.png',
    'loading.gif'
]

# with open(f'total_tintuc_linux.csv', 'w', encoding='utf-8') as f:
#     f.write('slug|title|time|category|content|image|img-src\n')

for url in article_list:
    print(f'Loop {loop}')
    # print(url)
    loop += 1
    driver.get(url)
    time.sleep(3)

    soup = BeautifulSoup(driver.page_source, 'html.parser')

    article_slug = url.split('/')[-1]
    os.makedirs(base_path + article_slug.split('.')[0])
    article_title = soup.find('h1', {'class': 'titleView2'})
    article_time = soup.find('time', {'itemprop': 'datePublished'})
    article_cat = 'Tin tức hoạt động'
    article_body = soup.find('div', {'itemprop': 'articleBody'})
    article_body = htmlmin.minify(str(article_body.prettify()), remove_comments=True, remove_empty_space=True)
    article_img = set()
    article_src = set()
    count = 1

    for link in soup.select("img"):
        lnk = link['src']
        
        if ' ' in link['src']:
            lnk = urllib.parse.quote(link['src'], safe=':/')
        elif 'upload' in link['src']:
            lnk = 'http://benhvienchinhhinh.net' + link['src']
        else:
            lnk = urllib.parse.quote(link['src'], safe=':/')

        if lnk.split('/')[-1] in ignore_img_list:
            continue

        if lnk.split('/')[-1].startswith('tin_tuc'):
            continue

        # if '?' in lnk.split('/')[-1].split('.')[-1]:
        #     lnk = lnk.split('?')[0]

        # if '%' in lnk.split('/')[-1].split('.')[-1]:
        #     lnk = lnk.split('%')[0]

        # article_img.add(lnk.split('/')[-1])

        try:
            # img_path = base_path + article_slug.split('.')[0] + '/' + lnk.split('/')[-1]
            if '?' in lnk.split('/')[-1].split('.')[-1]:
                # ./total-tin-tuc/slug/img-count.extension
                img_path = base_path + article_slug.split('.')[0] + '/' + article_slug.split('.')[0] + '-' + str(count) + '.'+ lnk.split('/')[-1].split('.')[-1].split('?')[0]
            elif '%' in lnk.split('/')[-1].split('.')[-1]:
                img_path = base_path + article_slug.split('.')[0] + '/' + article_slug.split('.')[0] + '-' + str(count) + '.'+ lnk.split('/')[-1].split('.')[-1].split('%')[0]
            else:
                img_path = base_path + article_slug.split('.')[0] + '/' + article_slug.split('.')[0] + '-' + str(count) + '.'+ lnk.split('/')[-1].split('.')[-1]
            
            article_img.add(lnk.split('/')[-1] + ',' + article_slug.split('.')[0] + '-' + str(count) + '.'+ lnk.split('/')[-1].split('.')[-1])

            article_src.add(link['src'] + ',' + 'https://benhvien1a.com/wp-content/uploads/sites/3/2021/07/' + article_slug.split('.')[0] + '-' + str(count) + '.'+ lnk.split('/')[-1].split('.')[-1])

            with open(img_path,'wb+') as f:
                try:
                    req = Request(url=lnk, headers=headers) 
                    html = urlopen(req).read()
                    f.write(html)
                    count+=1
                except:
                    print(lnk)
                    print(url)
        except Exception as err:
            print(lnk)
            print(url)
            print(err)  

        # article_path = './article/tintuc/' + article_slug.split('.')[0] + '.txt'
        # with open(article_path, 'w') as f:
        #     f.write(article_body)

    txt = article_slug.strip() + '|' + article_title.text.strip() + '|' + article_time.text.strip() + '|' + article_cat.strip() + '|' + article_body + '|' + '; '.join(i for i in article_img) + '|' + '; '.join(i for i in article_src) + '\n'
    
    with open(f'final_tintuc_linux.csv', 'a', encoding='utf-8') as f:
        f.write(txt)

driver.close()