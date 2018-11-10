import csv


list = []
with open('dataset1.csv') as csv_file:
    csv_reader = csv.reader(csv_file,delimiter=',')
    line_count = 0
    for row in csv_reader:
        list.append(row)


// Index 0 represents the columns names.
print(list[0])
