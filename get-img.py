img_set = set()

with open('E:/VM/ShareFolder/Working/web-crawl/crawl/6-sinhvien_1.csv', 'r', encoding='utf-8') as f:
    # line = f.readline()
    for line in f:
        img = line.split('|')[4]

        print(img)

        item = img.split(',')
        for i in item:
            img_set.add(i.strip())
        print('ok')

print(sorted(img_set))

with open('./demo.txt', 'a', encoding='utf-8') as fw:
    for i in sorted(img_set):
        fw.write(i + '\n')
        print('ok')

fw.close()