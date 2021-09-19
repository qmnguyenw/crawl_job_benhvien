'''
1. Fix: slug remove .html
2. Fix: title fix uppercase -> normal case
3. Set featured image = 1st img
4. Scheduled post 
5. Set author: nganguyen - userid: 8

~1. Mỗi bài post thì tiêu đề biến thành viết thường.~
2. Đặt featured image thì là cái image đầu tiên trong bài
~3. Scheduled bài post tuần tự theo ngày bắt đầu từ hôm nay~
~4. Đặt tác giả là nganguyen~
~5. cái URL slug hiện nay có cái đoạn "-html" ở cuối, bỏ đi~
'''

import csv
import datetime

# with open('./total_kienthuc_output.csv', 'r' , encoding='utf-8') as f_in, open('./new_kienthuc.sh', 'w', encoding='utf-8') as f_out:
with open('./total_tintuc_output.csv', 'r' , encoding='utf-8') as f_in, open('./new_tintuc.sh', 'w', encoding='utf-8') as f_out:
    reader = csv.reader(f_in, delimiter='|')
    
    count = 0

    # fieldnames = ['article_slug', 'article_title', 'article_time', 'article_cat', 'article_body', 'article_img', 'img_src']

    date = '26-07-2021'
    post_date = datetime.datetime.strptime(date, '%d-%m-%Y')

    for row in reader:
        count += 1
        
        post_name = row[0].split('.')[0]
        
        post_title = ''
        if(row[1].isupper()):
            # str.title() # They'Re Bill'S Friends From The Uk
            # string.capwords("they're bill's friends from the UK") # They're Bill's Friends From The Uk
            print(row[1])
            post_title = row[1].capitalize()
        else:
            post_title = row[1]
        
        post_date += datetime.timedelta(days=1) 
        post_date_str = post_date.strftime('%Y-%m-%d')
        if post_date > datetime.datetime.now():
            post_status = 'future'
        else:
            post_status = 'publish'

        # txt = 'wp --url=https://benhvien1a.com post create --post_name=\'' + post_name + '\' --post_title=\'' +  post_title +  '\' --post_status=\'' + post_status + '\' --post_date=\'' + post_date_str + '\' doc/kienthuc/' + post_name + '.txt' + ' --post_type=\'post\' --post_category=61 --post_author=8\n'
        txt = 'wp --url=https://benhvien1a.com post create --post_name=\'' + post_name + '\' --post_title=\'' +  post_title +  '\' --post_status=\'' + post_status + '\' --post_date=\'' + datetime.datetime.strptime(row[2], '%d-%m-%Y').strftime('%Y-%m-%d') + '\' doc/tintuc/' + post_name + '.txt' + ' --post_type=\'post\' --post_category=65 --post_author=8\n'

        f_out.write(txt)
        
    print(count)