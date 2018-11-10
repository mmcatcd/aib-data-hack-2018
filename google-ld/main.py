import re
from langdetect import detect
from textblob import TextBlob

def clean(text):
  return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", text).split())

def get_sentiment(text):
  analysis = TextBlob(clean(text))
  polarity = analysis.sentiment.polarity
  if polarity > 0:
    return 1
  else:
    return 0

sent = get_sentiment("my hair is blue")
print("Sentiment...")
print(sent)