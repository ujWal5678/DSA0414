import pandas as pd

df=pd.read_csv('creview.csv')

review = df['reviewText'].str.lower().str.split().explode().value_counts()
print(review)
