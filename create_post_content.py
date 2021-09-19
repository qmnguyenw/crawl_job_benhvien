import csv

with open('./total_tintuc_output.csv', 'r' , encoding='utf-8') as f_in:
    reader = csv.reader(f_in, delimiter='|')

    count = 0
    
    for row in reader:
        count+=1
        for article_title in row[0]:
            article_path = 'E:/VM/ShareFolder/Working/web-crawl/crawl/doc1/tintuc/' + row[0].split('.')[0] + '.txt'
            with open(article_path, 'w', encoding='utf-8') as f:
                f.write(row[-3])

    f.close()
    print(count)

