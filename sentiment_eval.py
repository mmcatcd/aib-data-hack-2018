import csv
import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import names

list =[]
with open('cleaned_data.csv',encoding='utf8',errors = 'ignore') as csv_file:
    csv_reader = csv.reader(csv_file,delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count!=0:
            tuple = (row[1],row[2])
            list.append(tuple)
        line_count += 1


values = []
for (words, sentiment) in list:
    words_filtered = [e.lower() for e in words.split() if len(e) >= 3]
    values.append((words_filtered, sentiment))


def get_words_in_sentences(values):
    all_words = []
    for (words, sentiment) in values:
      all_words.extend(words)
    return all_words

def get_word_features(wordlist):
    wordlist = nltk.FreqDist(wordlist)
    word_features = wordlist.keys()
    return word_features

word_features = get_word_features(get_words_in_sentences(values))


def extract_features(document):
    document_words = set(document)
    features = {}
    for word in word_features:
        features['contains(%s)' % word] = (word in document_words)
    return features


training_set = nltk.classify.apply_features(extract_features, values)
classifier = nltk.NaiveBayesClassifier.train(training_set)

final =[]
with open('test_data.csv',encoding='utf8',errors = 'ignore') as csv_file:
    csv_reader = csv.reader(csv_file,delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count==0:
            row[0] = 'id'
            row[1] = 'label'
        if line_count!=0:
            result = classifier.classify(extract_features(row[1].split()))
            row[1] = result
            print(row[1])
            print(result)
        line_count += 1
        final.append(row)

result = open('classifier.csv','w')
with result:
    writer = csv.writer(result)
    writer.writerows(final)
