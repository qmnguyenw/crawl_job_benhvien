import csv
from bs4 import BeautifulSoup

with open('./total_kienthuc_linux.csv', 'r' , encoding='utf-8') as f_in, open('./total_kienthuc_output.csv', 'r', encoding='utf-8') as f_out:
    reader_full = csv.reader(f_in, delimiter='|')
    reader_missing = csv.reader(f_out, delimiter='|')

    count = 0

    full_list = list()
    missing_list = list()

    for row in reader_full:
        full_list.append(row[0])
    for row in reader_missing:
        missing_list.append(row[0])

    output = [x for x in full_list if x not in missing_list]
        
    print(output)

"""
check replace or not 
"""


# import csv
# from bs4 import BeautifulSoup

# with open('./total_tintuc_linux.csv', "r", encoding="utf-8") as f:
#     reader = csv.reader(f, delimiter='|')
#     count = 0
#     for row in reader:
#         count+=1
        
#         parsed_html = BeautifulSoup(row[-3], features='lxml')

#         # print(parsed_html.select('img'))
#         for link in parsed_html.select('img'):
#             lnk = link['src']
#             print(lnk)
#         print('\n')
#         # img = row[-1].split(';')[0]
#         # row[-1].split(';')[1]
#         # print(row[-2])
        
#     print(count)