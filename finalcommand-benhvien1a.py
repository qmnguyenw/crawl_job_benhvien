import csv
import datetime

with open('./total_kienthuc_output.csv', 'r' , encoding='utf-8') as f_in, open('./final-command_kienthuc.sh', 'w', encoding='utf-8') as f_out:
    reader = csv.reader(f_in, delimiter='|')

    f_out.write('#!/bin/bash')
    count = 0

    for row in reader:
        time = (datetime.datetime.strptime(str, '%d-%m-%Y') + datetime.timedelta(days=1)).strftime('%Y-%m-%d')
        txt = 'wp --url=https://benhvien1a.com post create --post_name=\'' + row[0].split('.')[0] + '\' --post_title=\'' +  row[1] +  '\' --post_status=\'draft\' --post_date=\'' + datetime.datetime.strptime(row[2], '%d-%m-%Y').strftime('%Y-%m-%d') + '\' doc/kienthuc/' + row[0].split('.')[0] + '.txt' + ' --post_type=\'post\' --post_category=61 \n'
        f_out.write(txt)
        