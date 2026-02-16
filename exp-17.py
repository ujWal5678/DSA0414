import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('creview.csv')

review = df['reviewText'].str.lower().str.split().explode().value_counts()
remove=["the","and","is"]
rem_w= review[~review.index.isin(remove)]
print(rem_w)
print(rem_w.nlargest(5))

review=rem_w.nlargest(5)
plt.bar(review.index,review.values)
plt.xlabel("Words")
plt.ylabel("Frequency")
plt.title("Most Frequent Words")
plt.show()
