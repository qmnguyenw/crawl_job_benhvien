import re

with open('./5-giangvien.txt', 'r', encoding='utf-8') as f:
    lines = f.read()

    parts = re.split('\n\n', lines)

    for item in parts:
        name = item.split('\n')[0]
        role = item.split('\n')[1]
        email = item.split('\n')[2]
        phone = item.split('\n')[3]
        department = item.split('\n')[4]

        print('part')
    
        with open('5-giangvien.csv', 'a', encoding='utf-8') as f:
            f.write(name + ',' + role + ',' + email + ',' + phone + ',' + department + '\n')

print('ok')
        