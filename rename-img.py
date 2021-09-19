# import csv
# from bs4 import BeautifulSoup

# with open('./final_tintuc_linux.csv', 'r' , encoding='utf-8') as f_in, open('./total_tintuc_output.csv', 'w', encoding='utf-8') as f_out:
#     reader = csv.reader(f_in, delimiter='|')

#     count = 0
    
#     # f_out.write(f_in.readline())

#     # for row in reader:
#     #     print(row[1])
#     #     f_out.write(row[1]+'\n')
#         # f_out.write('|'.join(row)+'\n')
#         # print(row[-1])

#     for row in reader:
#         count+=1
#         if row[-1].strip() == '':
#             f_out.write('|'.join(row)+'\n')
#             continue
#         print(count, row[-1].split(';'))
#         for i in row[-1].split(';'):
#             # print(i.split(',')[0])
#             if(i.split(',')[0].strip() in row[-3]):
#                 row[-3] = row[-3].replace(i.split(',')[0].strip(),i.split(',')[1].strip())
#                 print('True')
#             else:
#                 print('False')
#         f_out.write('|'.join(row)+'\n')
#         print('\n')
#         # img = row[-1].split(';')[0]
#         # row[-1].split(';')[1]
#         # print(row[-2])
        
#     print(count)

"""
check replace or not 
"""


import csv
from bs4 import BeautifulSoup

import webbrowser
import requests

with open('./total_tintuc_output.csv', "r", encoding="utf-8") as f:
    reader = csv.reader(f, delimiter='|')
    count = 0
    for row in reader:
        count+=1
        
        parsed_html = BeautifulSoup(row[-3], features='lxml')

        # print(parsed_html.select('img'))
        for link in parsed_html.select('img'):
            lnk = link['src']
            # print(lnk)
            # webbrowser.open(lnk)
            r = requests.get(lnk)
            if r.status_code == 404:
                print(lnk)
        # print('\n')
        # img = row[-1].split(';')[0]
        # row[-1].split(';')[1]
        # print(row[-2])
        
    print(count)