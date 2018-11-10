import csv
import re

list = []

def clean(text):
  return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)|(\s[A-Za-z]{1}\s)", " ", text).split())

unwanted = {'WEBSITE2018','@USER','&quot'}
emoji_pattern = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
        u"WEBSITE2018"
        u"@USER"
                           "]+", flags=re.UNICODE)

with open('dataset2_final_eval.csv',encoding='utf8',errors = 'ignore') as csv_file:
    csv_reader = csv.reader(csv_file,delimiter=',')
    line_count = 0
    for row in csv_reader:
        row[1] = emoji_pattern.sub(r'',row[1])
        row[1] = clean(row[1])
        new_row = row[1].replace('&quot','')
        row[1] = new_row
        list.append(row)



cleaned_data = open('test_data.csv','w')
with cleaned_data:
    writer = csv.writer(cleaned_data)
    writer.writerows(list)
