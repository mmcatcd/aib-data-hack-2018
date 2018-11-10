from sklearn.linear_model import LinearRegression
import csv
import numpy as np
import pandas as pd


data = pd.read_csv('cleaned_data.csv')

input = data['text'].apply(lambda x:float(x))
output = data['sentiment']

input = input.values.reshape(len(input),1)
output = output.values.reshape(len(input),1)

print('Training...')
predictor = LinearRegression(n_jobs=-1)
predictor.fit(input,output)

print('Trained it...')


words = 'I am happy'
outcome = predictor.predict(X=words)
print(outcome)
