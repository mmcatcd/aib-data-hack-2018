import csv


list = []
unwanted = {'WEBSITE2018','@USER'}
with open('dataset1.csv') as csv_file:
    csv_reader = csv.reader(csv_file,delimiter=',')
    line_count = 0
    for row in csv_reader:
        text = row[1]
        list_text = text.split()
        row[1] = [e for e in list_text if e not in unwanted]
        list.append(row)



# Index 0 represents the columns names.
print(list[1])
print(list[2])
