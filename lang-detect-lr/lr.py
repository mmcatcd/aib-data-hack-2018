import csv
from sklearn.linear_model import LinearRegression

max_len = 500500

# Define dictionaries for languages
english = []
french = []
german = []
italian = []
portuguese = []
spanish = []
japanese = []

words = ['testing', 'hello', 'there']      

# English
i = 0
with open('data.en', encoding='utf8', errors='ignore') as f:
  reader = csv.reader(f, delimiter=' ')
  for line in reader:
    i+=1
    if i >= max_len:
      break

    for word in line:
      english.append(word)

# French
# i = 0
# with open('french.txt', encoding='utf8', errors='ignore') as f:
#   for line in f:
#     for word in line.split():
#       french.append(word)

# # German
# with open('german.txt', encoding='utf8', errors='ignore') as f:
#   for line in f:
#     for word in line.split():
#       german.append(word)

# # Italian
# with open('italian.txt', encoding='utf8', errors='ignore') as f:
#   for line in f:
#     for word in line.split():
#       italian.append(word)

# # Spanish
# with open('spanish.txt', encoding='utf8', errors='ignore') as f:
#   for line in f:
#     for word in line.split():
#       spanish.append(word)

# # Portuguese
# with open('pt.dic') as f:
#   for line in f:
#     for word in line.split():
#       portuguese.append(word)

# English language dataset

res = []
for word in english:
  res.append('en')

print('Read in english dictionary.')
print('Training model...')
predictor = LinearRegression(n_jobs=-1)
predictor.fit(X=english,y=res)

print('Trained model.')
print('Predicting...')
outcome = predictor.predict(X=words)

print(outcome)