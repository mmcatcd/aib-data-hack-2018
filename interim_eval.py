from langdetect import detect
import csv

list = []
lang  = {'en':1, 'fr':2,'de':3,'it':4,'pt':5,'es':6,'ja':7}
with open('cleaned_data.csv',encoding='utf8',errors = 'ignore') as csv_file:
    csv_reader = csv.reader(csv_file,delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            row[0] = 'id'
            row[1] = 'label'
        else:
            if row[1]!='':
                result = detect(row[1])
                if result in lang:
                    key_code = lang[result]
                    print(key_code)
                    row[1] = key_code
                else:
                    row[1] = '1'
            else:
                row[1] = '1'
        list.append(row)
        line_count+=1


result = open('result.csv','w')
with result:
    writer = csv.writer(result)
    writer.writerows(list)
