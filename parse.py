import csv
import re

list = []
unwanted = {'WEBSITE2018','@USER'}


emoji_pattern = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
        u"\U00010000-\U0010ffff"
                           "]+", flags=re.UNICODE)

with open('dataset1_final_eval.csv',encoding='utf8',errors = 'ignore') as csv_file:
    csv_reader = csv.reader(csv_file,delimiter=',')
    line_count = 0
    for row in csv_reader:
        row[1] = row[1].split()

        # removing @USER and hashtags
        row[1] = [e for e in row[1] if not (e.startswith('#') or e in unwanted)]
        text = row[1]
        i=0;
        new_row = ''
        while i < len(text):
            text[i]  = emoji_pattern.sub(r'',text[i])
            new_row = new_row +' ' +text[i]
            i +=1

        row[1] = new_row
        list.append(row)



cleaned_data = open('cleaned_data.csv','w')
with cleaned_data:
    writer = csv.writer(cleaned_data)
    writer.writerows(list)
# Index 0 represents the columns names.
print(list[601])
