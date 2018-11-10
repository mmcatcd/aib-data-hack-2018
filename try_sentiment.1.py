import csv
import re
from textblob import TextBlob
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

nltk.download('vader_lexicon')

sid = SentimentIntensityAnalyzer()

def clean(text):
  return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", text).split())


list = []
with open('cleaned_data.csv',encoding='utf8',errors = 'ignore') as csv_file:
    csv_reader = csv.reader(csv_file,delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count==0:
            row[0] = 'id'
            row[1] = 'label'
        if line_count!=0:
            value = sid.polarity_scores(row[1])
            print(value)
            #row[1] = value

        list.append(row)
        line_count +=1



result = open('sentiment_interim.csv','w')
with result:
    writer = csv.writer(result)
    writer.writerows(list)
